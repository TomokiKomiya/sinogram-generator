#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from scipy.spatial import distance
import numpy as np
from tqdm import tqdm
import time
import datetime
import sys
import os
import yaml

def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return 'ok'

def write_note_start(sphere_c, sphere_start, sphere_end, x_ray, detecta_sdd_x, detecta_w, detecta_h, projection_num, output_path):
    path = os.path.join(output_path, '{0}_{1}x{2}x{3}_data.txt'.format(output_path, detecta_w, detecta_h, projection_num))
    data = open(path, 'w+')
    data.write("start : " + str(datetime.datetime.now()))
    data.write("\nX-ray source position: {0}".format(x_ray))
    data.write("\nDistance to the detector: {0}".format(detecta_sdd_x))
    data.write("\nDistance to the object: {0}".format(sphere_c[0]))
    data.write("\nDetector panel size: {0}x{1}".format(detecta_w, detecta_h))
    data.write("\nSphere radius (start): {0}".format(sphere_start))
    data.write("\nSphere radius (end): {0}".format(sphere_end))
    data.write("\nNumber of projections: {0}".format(projection_num))
    data.close()
    return 'ok'

def write_note_end(file_name, elapsed_time, output_path, detecta_w, detecta_h, projection_num):
    path = os.path.join(output_path, '{0}_{1}x{2}x{3}_data.txt'.format(output_path, detecta_w, detecta_h, projection_num))
    data = open(path, 'a')
    data.write("\nSave file name: {0}".format(file_name))
    data.write("\ncreated: " + str(datetime.datetime.now()))
    data.write("\nelapsed_time: {0}".format(elapsed_time) + "[sec]")
    data.close()

def get_cross_point(sphere, r, detecta, x_ray):
    params = []
    sphere_x, sphere_y, sphere_z = sphere
    Ax, Ay, Az = x_ray
    Bx, By, Bz = detecta

    # 方向ベクトルを求める.
    ABx = Bx - Ax
    ABy = By - Ay
    ABz = Bz - Az

    # AB - Sphere
    Sx = Ax - sphere_x
    Sy = Ay - sphere_y
    Sz = Az - sphere_z

    A = ABx ** 2 + ABy ** 2 + ABz ** 2
    B = 2 * (Sx * ABx + Sy * ABy + Sz * ABz)
    C = Sx ** 2 + Sy ** 2 + Sz ** 2 - r ** 2

    try:
        # paramの解
        t1 = (-B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
        t2 = (-B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
        params.append(t1)
        params.append(t2)
        # 求める頂点 (X, Y, Z), 交点P1, P2
        point = []
        for i, t in enumerate(params):
            X = ABx * t + Ax
            Y = ABy * t + Ay
            Z = ABz * t + Az
            P = [X, Y, Z]
            point.append(P)

        return point

    except ValueError:
        point = []
        return point

def get_distance(point):
    x, y = point
    dis = distance.euclidean(x, y)
    return dis

def convert_transparent(d):
    I0 = 65535
    return I0 * math.exp(-d)

def min_max(x, axis=None):
    x_min = x.min(axis=axis, keepdims=True)
    x_max = x.max(axis=axis, keepdims=True)
    return (x - x_min) / (x_max - x_min)

def saveImage(data, path, x, y, z):
    path = os.path.join(path, path)
    data.tofile('./{0}-uint16_{1}x{2}x{3}.raw'.format(path, x, y, z))
    return '{0}-uint16_{1}x{2}x{3}.raw'.format(path, x, y, z)

def main(setting):
    start = time.time()
    # input
    sphere_c = setting['sphere_c']
    sphere_start = setting['sphere_start']
    sphere_end = setting['sphere_end']
    x_ray = setting['x_ray']
    detecta_sdd_x = setting['detecta_sdd_x']
    detecta_w = setting['detecta_w']
    detecta_h = setting['detecta_h']
    projection_num = setting['projection_num']
    output_path = setting['output_path']
    create_dir(output_path)
    # 変形幅
    deformation = sphere_end - sphere_start
    step = deformation / projection_num
    write_note_start(sphere_c, sphere_start, sphere_end, x_ray, detecta_sdd_x, detecta_w, detecta_h, projection_num, output_path)
    # output
    sinogram = []
    for d in tqdm(range(projection_num)):
        sinogram_h = []
        sphere_r = sphere_start + d * step
        for h in range(detecta_h):
            sinogram_w = []
            for w in range(detecta_w):
                detecta_ssd_y = - detecta_h / 2 + h
                detecta_ssd_z = - detecta_w / 2 + w
                detecta_point = [detecta_sdd_x, detecta_ssd_y, detecta_ssd_z]
                # 直線と球の交点を求める.
                point = get_cross_point(sphere_c, sphere_r, detecta_point, x_ray)
                if point == []:
                    dis = 0.0
                else:
                    # 交点のキョリを求める.
                    dis = get_distance(point)
                sinogram_w.append(dis)
            sinogram_h.extend(sinogram_w)
        sinogram.extend(sinogram_h)
    sinogram = np.array(sinogram)
    sinogram = min_max(sinogram)

    for i, data in enumerate(sinogram):
        sinogram[i] = convert_transparent(data)

    sinogram = sinogram.astype(np.uint16)
    file_name = saveImage(sinogram, output_path, detecta_w, detecta_h, projection_num)
    elapsed_time = time.time() - start
    write_note_end(file_name, elapsed_time, output_path, detecta_w, detecta_h, projection_num)
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")



if __name__ == '__main__':

    with open('setting.yml', 'r') as yml:
        setting = yaml.load(yml, Loader=yaml.SafeLoader)

    main(setting)