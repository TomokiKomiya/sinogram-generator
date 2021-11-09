import cv2
import numpy as np
import matplotlib.pyplot as plt

pic1=cv2.imread('sphere-horn-shunck-float-O(-54.1113,-54.1113,-54.6133)_250x250x252-0.43289x0.43289x0.43289.png',cv2.IMREAD_GRAYSCALE)
pic1=pic1.astype(np.float32)
pic2=cv2.imread('sphere-r27.5-float-O(-54.1113,-54.1113,-54.6133)_250x250x252-0.43289x0.43289x0.43289.png',cv2.IMREAD_GRAYSCALE)
pic2=pic2.astype(np.float32)

#輝度差し引き
pic3=pic2-pic1
pic3=np.where(pic3<0,0,pic3)
pic3=pic3.astype(np.uint8)

print(pic3.min())
print(pic3.max())
print(pic3)

cv2.imwrite('diff-ct-volume-horn-shunch-f2.png', pic3)