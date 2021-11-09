import numpy as np
import math
from tqdm import tqdm
import argparse

def saveImage(save_data, file_name, x, y, z):
    print(save_data.shape)
    print(save_data.dtype)
    save_data.tofile('./{0}_{1}x{2}x{3}.raw'.format(file_name, x, y, z))
    return "Successfully save data"

def input_raw(path, x, y, z, type):
    fd = open(path, 'rb')
    f = np.fromfile(fd, dtype=type, count=x*y*z)
    # img = f.reshape((z, y, x))
    img = f
    fd.close()
    print(img.shape)
    print(img.dtype)
    return img

def convert_transparent(d):
    I0 = 65535
    return I0 * math.exp(-d)

def min_max(x, axis=None):
    x_min = x.min(axis=axis, keepdims=True)
    x_max = x.max(axis=axis, keepdims=True)
    return (x - x_min) / (x_max - x_min)

def create_sino(projection_img, output_path, x, y, z):
    # uint16の時
    projection_img = min_max(projection_img)
    for i in tqdm(range(projection_img.shape[0])):
        projection_img[i] = convert_transparent(projection_img[i])
    print(projection_img.shape)
    projection_img = projection_img.astype(np.uint16)
    res = saveImage(projection_img, output_path, x, y, z)
    print(res)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--intput_file',
        type = str,
        required=True,
        help='input path'
    )
    parser.add_argument(
        '-o',
        '--output_file',
        type = str,
        required=True,
        help='output path'
    )

    args = parser.parse_args()
    # params
    input_path = args.intput_file
    output_path = args.output_file
    x = 512
    y = 512
    z = 512
    d_type = np.uint16

    print("Input Path: ", input_path)
    print("Output Path: ", output_path)

    data = input_raw(input_path, x, y, z, d_type)

    create_sino(data, output_path, x, y, z)

if __name__ == '__main__':
    main()