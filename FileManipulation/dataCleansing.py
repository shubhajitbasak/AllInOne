import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from sklearn.model_selection import train_test_split
import glob
import os
import warnings
import OpenEXR
import Imath
# import numpy
warnings.filterwarnings("error")




baseFemalePath = r"D:\project1\dataCreation\Data\female"
baseMalePath = r"D:\project1\dataCreation\Data\male"

baseExpDataPath = r'D:\project1\dataCreation\Data\data'

baseExpExrDataPath = r'D:\project1\dataCreation\Data\data_exr'
baseExpExrDataPathMale = r'D:\project1\dataCreation\Data\data_exr\male'
baseExpExrDataPathFemale = r'D:\project1\dataCreation\Data\data_exr\female'

# --------convert png to jpg --------------#

# for dir, subdirs, files in os.walk(baseFemalePath):
#     for f in files:
#         if '.png' in f:
#             if 'rgb' in f:
#                 im1 = Image.open(os.path.join(dir, f))
#                 if not im1.mode == 'RGB':
#                     im1 = im1.convert('RGB')
#                 print(os.path.join(dir, f))
#                 # print(os.path.join(dir, f).split('.')[0] + '.jpg')
#                 im1.save(os.path.join(dir, f).split('.')[0] + '.jpg')
#                 # print(os.path.join(dir, f))
#                 os.remove(os.path.join(dir, f))

#-------------- remove png text blender log --------------------#

# for dir, subdirs, files in os.walk(baseExpExrDataPath):
#     for f in files:
#         if '.png' in f:
#             # print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))
#         if 'blender.log' in f:
#             # print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))
#         if '.txt' in f:
#             # print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))

# ----------------  fix depth issue in png files -----------------#

#
# for dir, subdirs, files in os.walk(baseMalePath):
#     for f in files:
#         if '.png' in f:
#             if 'depth' in f:
#                 im1 = cv2.imread(os.path.join(dir, f), 0)
#                 print(os.path.join(dir, f))
#                 test = 10/im1
#                 mask = np.asarray(im1 == 0, dtype=np.uint8)
#                 dst = cv2.inpaint(im1, mask, 3, cv2.INPAINT_TELEA)
#                 print(os.path.join(dir, f))
#                 cv2.imwrite(os.path.join(dir, f), dst)
#                 # im2 = img.imread(os.path.join(dir, f))
#                 # test = 100/im2
#                 # print(im2.shape)


# for dir, subdirs, files in os.walk(baseExpDataPath):
#     for f in files:
#         if '.png' in f:
#             if 'depth' in f:
#                 im1 = cv2.imread(os.path.join(dir, f), 0)
#                 try:
#                     test = 10/im1
#                 except RuntimeWarning:
#                     print(os.path.join(dir, f))

# im1 = cv2.imread(os.path.join(dir, f), 0)
# test = 10 / im1
# mask = np.asarray(im1 == 0, dtype=np.uint8)
# dst = cv2.inpaint(im1, mask, 4, cv2.INPAINT_TELEA)
# # print(os.path.join(dir, f))
# cv2.imwrite(os.path.join(dir, f), dst)


# -------------- read exr files -------------------- #




# your filename here 'data/depthExr0022.exr'

# def readExr(filepath):
#     exrimage = OpenEXR.InputFile(filepath)
#     dw = exrimage.header()['dataWindow']
#     (width, height) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
#
#     def fromstr(s):
#         mat = np.frombuffer(s, dtype=np.float16)
#         mat = mat.reshape(height, width)
#         return mat
#
#     pt = Imath.PixelType(Imath.PixelType.HALF)
#     (r, g, b) = [fromstr(s) for s in exrimage.channels('RGB', pt)]
#
#     return r, g, b

# test = cv2.imread('data/DptMp_A_00_S_00_F_0403_L.exr', cv2.IMREAD_UNCHANGED)
# test1 = cv2.imread('data/depthExr0000.exr', cv2.IMREAD_UNCHANGED)
# for dir, subdirs, files in os.walk(baseFemalePath):
#     for f in files:
#         if '0008.exr' in f:
#             test = cv2.imread(os.path.join(dir, f), cv2.IMREAD_UNCHANGED)
#             # r, g, b = readExr(os.path.join(dir, f))
#             # im1 = np.asanyarray(r, dtype=np.float64)
#
#             if(test.min() > 1000):
#                 print(os.path.join(dir, f))
#                 print(test.min())

# r1, g1, b1 = readExr('data/DptMp_A_00_S_00_F_0403_L.exr')
# r2, g2, b2 = readExr('data/depthExr0000.exr')
# #
# im1 = np.asanyarray(r1, dtype=np.float64)
# # x1 = np.clip(r1, 0, 5)
# im2 = np.asanyarray(r2, dtype=np.float64)
# #
# plt.subplot(221), plt.imshow(test)
# plt.subplot(222), plt.imshow(test1)
# #
# plt.show()

# print('test')

#----------- Data preparation ----------------------- #

count = 0
textFileData = []

for folder in next(os.walk(baseExpExrDataPathMale))[1]:
    basePath = os.path.join(baseExpExrDataPathMale, folder)
    # print(basePath)
    for subfolder in next(os.walk(basePath))[1]:
        baseTempPath = os.path.join(basePath, subfolder)
        depthExrCount = len(glob.glob1(baseTempPath, "depthExr*.exr"))
        rgbCount = len(glob.glob1(baseTempPath, "rgb*.jpg"))
        # depthPngCount = len(glob.glob1(baseTempPath, "depth*.png"))
        # dataFileCount = len(glob.glob1(baseTempPath, "data*.txt"))

        listCount = [rgbCount, depthExrCount]

        if all(x == 71 for x in listCount):
            print("\n Folder : {0} -------- EXR Count : {1}".format(baseTempPath, depthExrCount))

            print(" \n Folder : {0} -------- RGB Count : {1}".format(baseTempPath, rgbCount))

            # print(" \n Folder : {0} -------- DEPTH PNG Count : {1}".format(baseTempPath, depthPngCount))

            # print(" \n Folder : {0} -------- Data Count : {1}".format(baseTempPath, dataFileCount))

            count = count + 1
            for i in range(72):
                # print(i)
                # depth = f"depth{i:04d}.png"
                # rgb = f"rgb{i:04d}.png"

                depthPath = os.path.join(baseTempPath, f"depthExr{i:04d}.exr")
                rgbPath = os.path.join(baseTempPath, f"rgb{i:04d}.jpg")

                if os.path.exists(rgbPath) and os.path.exists(depthPath):
                    # print(depthPath)
                    # print(rgbPath)

                    tData = str(rgbPath) + ',' + str(depthPath)
                    tData = tData.replace("D:\\project1\\dataCreation\\Data\\","")
                    tData = tData.replace("\\","/")
                    textFileData.append(tData)
print(count)


for folder in next(os.walk(baseExpExrDataPathFemale))[1]:
    basePath = os.path.join(baseExpExrDataPathFemale, folder)
    # print(basePath)
    for subfolder in next(os.walk(basePath))[1]:
        baseTempPath = os.path.join(basePath, subfolder)
        depthExrCount = len(glob.glob1(baseTempPath, "depthExr*.exr"))
        rgbCount = len(glob.glob1(baseTempPath, "rgb*.jpg"))
        # depthPngCount = len(glob.glob1(baseTempPath, "depth*.png"))
        # dataFileCount = len(glob.glob1(baseTempPath, "data*.txt"))

        listCount = [rgbCount, depthExrCount]

        if all(x == 71 for x in listCount):
            print("\n Folder : {0} -------- EXR Count : {1}".format(baseTempPath, depthExrCount))

            print(" \n Folder : {0} -------- RGB Count : {1}".format(baseTempPath, rgbCount))

            # print(" \n Folder : {0} -------- DEPTH PNG Count : {1}".format(baseTempPath, depthPngCount))

            # print(" \n Folder : {0} -------- Data Count : {1}".format(baseTempPath, dataFileCount))

            count = count + 1
            for i in range(72):
                # print(i)
                # depth = f"depth{i:04d}.png"
                # rgb = f"rgb{i:04d}.png"

                depthPath = os.path.join(baseTempPath, f"depthExr{i:04d}.exr")
                rgbPath = os.path.join(baseTempPath, f"rgb{i:04d}.jpg")

                if os.path.exists(rgbPath) and os.path.exists(depthPath):
                    # print(depthPath)
                    # print(rgbPath)

                    tData = str(rgbPath) + ',' + str(depthPath)
                    tData = tData.replace("D:\\project1\\dataCreation\\Data\\","")
                    tData = tData.replace("\\","/")
                    textFileData.append(tData)


data_train, data_test = train_test_split(textFileData, test_size=0.20, random_state=42)


with open(r'D:\project1\dataCreation\Data\data_exr\data_train.csv', 'a') as fd:

    for item in data_train:
        fd.write(item)
        fd.write("\n")

with open(r'D:\project1\dataCreation\Data\data_exr\data_test.csv', 'a') as fd:

    for item in data_test:
        fd.write(item)
        fd.write("\n")