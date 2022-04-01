# importing pyplot and image from matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2
from PIL import Image
import os
import re
import numpy as np
from io import BytesIO
from zipfile import ZipFile

import scipy
# import sklearn
# from sklearn.feature_extraction import image
from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# import OpenEXR
# import Imath
import numpy


# your filename here 'data/depthExr0022.exr'
#
# def readExr(filepath):
#     exrimage = OpenEXR.InputFile(filepath)
#     dw = exrimage.header()['dataWindow']
#     (width, height) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
#
#     def fromstr(s):
#         mat = numpy.fromstring(s, dtype=numpy.float16)
#         mat = mat.reshape(height, width)
#         return mat
#
#     pt = Imath.PixelType(Imath.PixelType.HALF)
#     (r, g, b) = [fromstr(s) for s in exrimage.channels('RGB', pt)]
#
#     return r, g, b


#
# depthFemale = cv2.imread('data/female/depthExr0000.exr', cv2.IMREAD_UNCHANGED)
#
# depthMale = cv2.imread('data/male/depthExr0000.exr', cv2.IMREAD_UNCHANGED)
#
#
# depthFemale

# r1, g1, b1 = readExr('data/depthExr0000.exr')
# r2, g2, b2 = readExr('data/depthExr0048.exr')
#
# im1 = np.asanyarray(r1, dtype=np.float64)
# x1 = np.clip(r1, 0, 5)
# im2 = np.asanyarray(x1, dtype=np.float64)
#
# plt.subplot(221), plt.imshow(im1)
# plt.subplot(222), plt.imshow(im2)
#
# plt.show()
#
# print('test')
# images = loadmat('data/Mat_1.mat',variable_names='IMAGES',appendmat=True).get('IMAGES')
# imgplot = plt.imshow(images[:,:,0])
# plt.show()


# for dir, subdirs, files in os.walk(r'D:\project1\dataCreation\Data\train'):
#     for f in files:
#         if "depth" in f:
#             filePath = os.path.join(dir, f)
#             # print(filePath)
#
#             src = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
#             # print(src.shape)
#
#             if(src.shape == (480,640,4)):
#                 print(filePath)
#                 print(src.shape)
#
#                 single_channel = src[:, :, 0]
#                 # print(single_channel.shape)
#                 cv2.imwrite(filePath, single_channel)
#
#             #extract red channel
#             # single_channel = src[:,:,0]
#
#             #write red channel to greyscale image
#             # cv2.imwrite(filePath,single_channel)


# im13 = np.asarray(Image.open(BytesIO(data['1.jpg'])))
# im14 = np.asarray(Image.open(BytesIO(data['1.png'])))

# im1 = img.imread("data/depth0056.png")
# mask = np.asarray(im1==0, dtype=np.uint8)
# dst = cv2.inpaint(im1, mask,3,cv2.INPAINT_TELEA)
# print(type(dst))
# img = Image.fromarray(dst, 'L')
# img.show()


# plt.imsave("data/depth0056_new.png",dst)
# # cv2.imwrite("data/depth0056_new.png",dst)
# im2 = img.imread("data/depth0056_new.png")
# print(im2.shape)

# plt.subplot(221),plt.imshow(im1)
# plt.subplot(222), plt.imshow(im2)
# plt.subplot(223),plt.imshow(dst)
# plt.show()


# im2 = 100/im1
# im2 = img.imread(r"D:\project1\dataCreation\Others\Code\Repo\bts\pytorch\result_bts_nyu_v2_pytorch_densenet161\raw\bathroom_rgb_00045.png")
# print('test')

# im3 = img.imread("data/1.jpg")
# im4 = img.imread("data/1.png")

# img1 = cv2.imread('data/depth0056.png')
# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = img.imread('data/depth0056.png')
# x1 = 100/img
# mask = np.asarray(img==0, dtype=np.uint8)
# dst = cv2.inpaint(img, mask,3,cv2.INPAINT_TELEA)
# #
# # dst = cv2.fastNlMeansDenoising(img,None,20,7,21)
# #
# print(dst.shape)
# #
# x2 = 100/dst
# cv2.imwrite('data/depth0056_new.png',dst)


# im1 = img.imread("D:/project1/dataCreation/Data/data/train/female/0018/Angry/depth0038.png")
# im2 = img.imread("data/Image_0010000.png")
# im3 = img.imread("data/Image0000.jpg")
#


# ---------- Image Resize ------------------ #

# from PIL import Image
# import numpy as np
# from resizeimage import resizeimage
# with open('data/test2.jpg', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [640, 480])
#         p= cover.save('data/test2_new.jpg', image.format)


# im1 = cv2.imread("data/test1.jpg")
# # test = 10/im1
#
# img = cv2.resize(im1,(640,480))
#
# cv2.imwrite("data/test1New.jpg", img)

# mask = np.asarray(im1 == 0, dtype=np.uint8)
# dst = cv2.inpaint(im1, mask, 4, cv2.INPAINT_TELEA)
# # print(os.path.join(dir, f))
# cv2.imwrite("D:/project1/dataCreation/Data/male/0003/Happy/depth0047.png", dst)
#
#
# # try:
# #     test = 100/im1
# # except Warning:
# #     print('warning raised')
# plt.subplot(221), plt.imshow(im1)
# plt.subplot(222), plt.imshow(mask)
# # plt.subplot(223),plt.imshow(img2)
# plt.show()


### ------------- Change the pixel values of an image ---------------------- ###

#
# im = Image.open('data/difOpac.png')
# im.show()
# pixelMap = im.load()
#
# img = Image.new(im.mode, im.size)
# pixelsNew = img.load()
# for i in range(im.size[0]):
#     for j in range(im.size[1]):
#         if pixelMap[i,j][-1] > 0:
#             l = list(pixelMap[i,j])
#             l[-1] = 255
#             pixelMap[i, j] = tuple(l)
#         pixelsNew[i,j] = pixelMap[i,j]
# im.close()
# img.show()
# img.save("data/out.png")
# img.close()

import matplotlib.pyplot as plt
test = np.load('/mnt/sata/dockerVolume/3DFace/test.np.npy')
print(test.shape)
plt.imshow(test)
plt.show()