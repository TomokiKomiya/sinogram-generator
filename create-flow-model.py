import numpy as np
from tqdm import tqdm

def saveImage(save_data, num, projection, x, y):
    save_data = np.array(save_data, dtype=np.float32)
    file_name = 'test-flow2/lobster-test-sino-{0}-float32'.format(projection)
    save_data.tofile('./{0}_{1}x{2}x{3}.raw'.format(file_name, x, y, num))
    return "Successfully save data"

def input_raw(path, x, y, z):
    fd = open(path, 'rb')
    f = np.fromfile(fd, dtype=np.float32, count=x*y*z)
    img = f.reshape((z, y, x))
    fd.close()
    print(img.shape)
    print(img.dtype)
    return img

def create_flow(data, projection, x, y, z):
    d_num = int(z/projection)
    print(d_num)
    for i in tqdm(range(projection)):
        box_elm = []
        for d in range(d_num):
            box_elm.append(data[d * projection + i].tolist())
        res = saveImage(box_elm, d_num, i, x, y)
    print(res)


# def create_flow_back(data, projection, z):
#     d_num = int(z/projection)
#     print(d_num)
#     box_all = []
#     for i in tqdm(range(projection)):
#         box_elm = []
#         for d in range(d_num):
#             box_elm.append(data[d * projection + i].tolist())
#         box_all.append(box_elm)
#     box = np.array(box_all, dtype=np.float32)
#     print(box.shape)
#     for i in tqdm(range(box.shape[0])):
#         res = saveImage(box[i], d_num, i)
#         print(res)
#     # print(box.reshape(d_num, 128,128))

def main():
    # params
    projection = 1024
    input_path = "./corrected_lobster-0_10240-sinogram_128x128x10240-0.400000-1.raw"
    x = 128
    y = 128
    z = 10240

    data = input_raw(input_path, x, y, z)

    create_flow(data, projection, x, y, z)

if __name__ == '__main__':
    main()

