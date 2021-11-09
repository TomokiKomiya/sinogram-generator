import numpy as np

def saveImage(save_data, start, end, num, offset):
    file_name = './lobster-sino-{0}_{1}-float32'.format(start + offset, end + offset)
    print(save_data.shape)
    print(save_data.dtype)
    save_data.tofile('./{0}_{1}x{2}x{3}.raw'.format(file_name, 1024, 1024, num))
    return "Successfully save data"

def input_raw(path, x, y, z):
    fd = open(path, 'rb')
    f = np.fromfile(fd, dtype=np.float32, count=x*y*z)
    img = f.reshape((z, y, x))
    fd.close()
    print(img.shape)
    print(img.dtype)
    return img

def devide_data(data, projection, z, offset):
    num = int(z/projection)
    print("{0}分割".format(num))
    for i in range(num):
        print('-----------{0}-----------'.format(i))
        start = i*projection
        end = (1 + i)*projection
        print('start: {0}'.format(start))
        print('end: {0}'.format(end))
        devide_data = data[start:end, :, :]
        print(devide_data.shape)
        # save image
        res = saveImage(devide_data, start, end, projection, offset)
        print(res)


def main():
    # params
    offset = 0
    projection = 1024
    input_path = "./corrected_lobster-0_10240-sinogram_1024x1024x10240-0.400000.raw"
    x = 1024
    y = 1024
    z = 10240

    data = input_raw(input_path, x, y, z)

    devide_data(data, projection, z, offset)

if __name__ == '__main__':
    main()