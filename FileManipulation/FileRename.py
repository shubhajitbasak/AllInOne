import os
import glob
import csv

# baseFemalePath = r"E:\Shubhajit_Data\From_SBASAK01-GWY1\FaceDepthSynth\female"
# baseMalePath = r"E:\Shubhajit_Data\From_SBASAK01-GWY1\FaceDepthSynth\male"

# baseFileTrainPathMale = r"D:\project1\dataCreation\Data\data\train\male"
# baseFileTrainPathFemale = r"D:\project1\dataCreation\Data\data\train\female"
# #
# baseFileTestPathFemale = r"D:\project1\dataCreation\Data\data\test\female"
# baseFileTestPathMale = r"D:\project1\dataCreation\Data\data\test\male"

# baseTrainPath = r"D:\project1\dataCreation\Data\train"


# for dir, subdirs, files in os.walk(baseMalePath):
#     for f in files:
#         #         f_new = f + 'bak'
#         #         os.rename(os.path.join(root, f), os.path.join(root, f_new))
#         #         print(f)
#         if '.png' in f:
#             if 'Image' in f:
#                 f_new = f.replace('Image', 'rgb')
#                 f0 = f_new.split('.')[0]
#                 f1 = f_new.split('.')[1]
#                 f2 = f_new.split('.')[2]
#                 # f_new = f1 + '_' + f0 + '.' + f2
#                 f_new = f1 + f0 + '.' + f2
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 # print(f_new)
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#             if 'test' in f:
#                 f_new = f
#                 if len(f.split('_')[1].split('.')[0]) < 4:
#                     t = f.split('_')[1].split('.')[0]
#                     t_n = '0' + t
#                     f_new = f_new.replace(t, t_n)
#                 f_new = f_new.replace('test_', 'depth.')
#                 #                 print(f_new)
#                 f0 = f_new.split('.')[0]
#                 f1 = f_new.split('.')[1]
#                 f2 = f_new.split('.')[2]
#                 # f_new = f1 + '_' + f0 + '.' + f2
#                 f_new = f1 + f0 + '.' + f2
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 # print(f_new)
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))


# for dir, subdirs, files in os.walk(baseFemalePath):
#     for f in files:
#         if '.png' in f:
#             if 'Image' in f:
#                 f_new = f.replace('Image', 'rgb')
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#             if 'test' in f:
#                 f_new = f
#                 if len(f.split('_')[1].split('.')[0]) < 4:
#                     t = f.split('_')[1].split('.')[0]
#                     t_n = '0' + t
#                     f_new = f_new.replace(t, t_n)
#                 f_new = f_new.replace('test_', 'depth')
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#         if '.txt' in f:
#             f_new = f
#             # print(f)
#             # print(dir)
#             if len(f.split('_')[1].split('.')[0]) < 4:
#                 t = f.split('_')[1].split('.')[0]
#                 t_n = '0' + t
#                 f_new = f_new.replace(t, t_n)
#             f_new = f_new.replace('test_', 'data')
#             # print(os.path.join(dir, f), os.path.join(dir, f_new))
#             os.rename(os.path.join(dir, f), os.path.join(dir, f_new))

# keys = ["image",'depth','Image'] # "rgb",
# for dir, subdirs, files in os.walk(baseFemalePath):
#     for f in files:
#         # if any(i in f for i in keys):
#         #     print(dir,f)
#         if 'rgb0' in f:
#             # print(f)
#             # print(dir, f)
#             f_new = f.replace('rgb', 'rgb_')
#             print(f_new)
#             os.rename(os.path.join(dir, f), os.path.join(dir, f_new))

# if '.txt' in f:
#     f_new = f
#     if len(f.split('.')[0]) > 8:
#         f_new = 'data' + f_new.split('.')[0].split('data')[1][1:] + '.txt'
#         # print(os.path.join(dir, f), os.path.join(dir, f_new))
#         os.rename(os.path.join(dir, f), os.path.join(dir, f_new))

# for dir, subdirs, files in os.walk(baseMalePath):
#     for f in files:
#         #         f_new = f + 'bak'
#         #         os.rename(os.path.join(root, f), os.path.join(root, f_new))
#         #         print(f)
#         if '.png' in f:
#             if 'depth' in f:
#                 s0 = 'depth'
#                 s1 = f.split(".")[0].split("depth")[0]
#                 s2 = '.png'
#                 f_new = s0 + s1 + s2
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#
#             if 'rgb' in f:
#                 s0 = 'rgb'
#                 s1 = f.split(".")[0].split("rgb")[0]
#                 s2 = '.png'
#                 f_new = s0 + s1 + s2
#                 # print(os.path.join(dir, f), os.path.join(dir, f_new))
#                 os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#
#         # if '.exr' in f:
#         #     if 'depth' in f:
#         #         s0 = 'depth'
#         #         s1 = f.split(".")[0].split("depth")[1]
#         #         s2 = '.png'
#         #         f_new = s1 + s0 + s2
#         #         os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#
#         # if '.txt' in f:
#         #     f_new = f
#         #     # print(f)
#         #     # print(dir)
#         #     if len(f.split('_')[1].split('.')[0]) < 4:
#         #         t = f.split('_')[1].split('.')[0]
#         #         t_n = '0' + t
#         #         f_new = f_new.replace(t, t_n)
#         #     f_new = f_new.replace('test_', 'data')
#         #     # print(os.path.join(dir, f), os.path.join(dir, f_new))
#         #     os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
#


# count = 0
# textFileData = []
#
# for folder in next(os.walk(baseMalePath))[1]:
#     subjectPath = os.path.join(baseMalePath, folder)
#     for subfolder in next(os.walk(subjectPath))[1]:
#         backgroundPath = os.path.join(subjectPath, subfolder)
#         if subfolder == 'Complex':
#             continue
            # for subfolder in next(os.walk(backgroundPath))[1]:
            #     complexEnvPath = os.path.join(backgroundPath, subfolder)
            #     # print(complexEnvPath)
            #     for subfolder in next(os.walk(complexEnvPath))[1]:
            #         expPath = os.path.join(complexEnvPath, subfolder)
            #         for subfolder in next(os.walk(expPath))[1]:
            #             # if subfolder == 'HeadRot':
            #
            #             cameraPath = os.path.join(expPath, subfolder)
            #             # print(cameraPath)
            #
            #             # exrList = glob.glob1(cameraPath, "*.exr")
            #             #
            #             # for f in exrList:
            #             #     f_new = f.replace('exr.exr', 'exr')
            #             #     print(f_new)
            #             #     os.rename(os.path.join(cameraPath, f), os.path.join(cameraPath, f_new))
            #             #
            #             #     if len(f.split('.')[0]) > 12:
            #             #         print(cameraPath, f)
            #             #         # f_new = f.split('.')[0][:-4].replace('depthExr', 'depthExr_') + '.exr'
            #             #         # print(f_new)
            #             #         # os.rename(os.path.join(cameraPath, f), os.path.join(cameraPath, f_new))
            #             #
            #             # rgbList = glob.glob1(cameraPath, "*.jpg")
            #             #
            #             # for f in rgbList:
            #             #     # if 'Image' in f:
            #             #     f_new = f.replace('jpg.jpg', 'jpg')
            #             #     print(f_new)
            #             #     os.rename(os.path.join(cameraPath, f), os.path.join(cameraPath, f_new))
            #             #
            #             #     if len(f.split('.')[0]) > 7:
            #             #         print(cameraPath, f)
            #             #         # f_new = f.split('.')[0][:-4].replace('image', 'rgb_') + '.jpg'
            #             #         # print(f_new)
            #             #         # os.rename(os.path.join(cameraPath, f), os.path.join(cameraPath, f_new))
            #
            #             depthExrCount = len(glob.glob1(cameraPath, "depthExr_*.exr"))
            #             rgbCount = len(glob.glob1(cameraPath, "rgb_*.jpg"))
            #             depthPngCount = len(glob.glob1(cameraPath, "depth_*.png"))
            #             dataFileCount = len(glob.glob1(cameraPath, "data_*.txt"))
            #
            #             if not (rgbCount == depthPngCount == depthExrCount == dataFileCount):
            #
            #                 print(cameraPath, rgbCount, depthPngCount, depthExrCount, dataFileCount)
        # else:
        #     for subfolder in next(os.walk(backgroundPath))[1]:
        #         expPath = os.path.join(backgroundPath, subfolder)
        #         for subfolder in next(os.walk(expPath))[1]:
        #             cameraPath = os.path.join(expPath, subfolder)
        #             # print(cameraPath)
        #             depthExrCount = len(glob.glob1(cameraPath, "depthExr_*.exr"))
        #             rgbCount = len(glob.glob1(cameraPath, "rgb_*.jpg"))
        #             depthPngCount = len(glob.glob1(cameraPath, "depth_*.png"))
        #             dataFileCount = len(glob.glob1(cameraPath, "data_*.txt"))
        #
        #             if not (rgbCount == depthPngCount == depthExrCount == dataFileCount):
        #
        #                 print(cameraPath, rgbCount, depthPngCount, depthExrCount, dataFileCount)

#
#         listCount = [rgbCount, depthPngCount]
#
#         if all(x == 71 for x in listCount):
#             # print("\n Folder : {0} -------- EXR Count : {1}".format(baseTempPath, depthExrCount))
#
#             print(" \n Folder : {0} -------- RGB Count : {1}".format(baseTempPath, rgbCount))
#
#             print(" \n Folder : {0} -------- DEPTH PNG Count : {1}".format(baseTempPath, depthPngCount))
#
#             # print(" \n Folder : {0} -------- Data Count : {1}".format(baseTempPath, dataFileCount))
#
#             count = count + 1
#             for i in range(72):
#                 # print(i)
#                 # depth = f"depth{i:04d}.png"
#                 # rgb = f"rgb{i:04d}.png"
#
#                 depthPath = os.path.join(baseTempPath, f"depth{i:04d}.png")
#                 rgbPath = os.path.join(baseTempPath, f"rgb{i:04d}.jpg")
#
#                 if os.path.exists(rgbPath) and os.path.exists(depthPath):
#                     # print(depthPath)
#                     # print(rgbPath)
#
#                     tData = str(rgbPath) + ',' + str(depthPath)
#                     tData = tData.replace("D:\\project1\\dataCreation\\Data\\","")
#                     tData = tData.replace("\\","/")
#                     textFileData.append(tData)
# print(count)


# for dir, subdirs, files in os.walk(baseFileTestPathMale):
#     for f in files:
#         if '.txt' in f:
#             print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))
#
#         if '.exr' in f:
#             print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))
#
#         if '.log' in f:
#             print(os.path.join(dir, f))
#             os.remove(os.path.join(dir, f))


# textFileData = []
#
# for folder in next(os.walk(baseFileTrainPathMale))[1]:
#
#     basePath = os.path.join(baseFileTestPathFemale, folder)
#     print(basePath)
#
#     for subfolder in next(os.walk(basePath))[1]:
#         baseTempPath = os.path.join(basePath, subfolder)
#
#         for i in range(72):
#             # print(i)
#             # depth = f"depth{i:04d}.png"
#             # rgb = f"rgb{i:04d}.png"
#
#             depthPath = os.path.join(baseTempPath, f"depth{i:04d}.png")
#             rgbPath = os.path.join(baseTempPath, f"rgb{i:04d}.png")
#
#             if os.path.exists(rgbPath) and os.path.exists(depthPath):
#                 # print(depthPath)
#                 # print(rgbPath)
#
#                 tData = str(rgbPath) + ',' + str(depthPath)
#                 tData = tData.replace("C:\\Users\\sbasak\\Desktop\\", "")
#                 tData = tData.replace("\\", "/")
#                 textFileData.append(tData)
#
# print(textFileData[0:5])
#
# with open(r'D:\project1\dataCreation\Data\data\test.csv', 'a') as fd:
#
#     for item in textFileData:
#         fd.write(item)
#         fd.write("\n")


# with open(r'D:\Project2(2Dto3D)\Data\Now_Challenge\imagepathsvalidation.txt') as f:
#     list = f.readlines()


# import numpy as np
#
# x = np.load(r'C:\Users\sbasak\Downloads\Deep3DFaceReconPyTorchcomputeddistances.npy')
#
# basePath = r'D:\Project2(2Dto3D)\Data\Now_Challenge\NoW_Dataset\final_release_version\detected_face'
#
# for dir, subdirs, files in os.walk(basePath):
#     if len(files) > 0:
#         for file in files:
#             tmp = np.load(os.path.join(dir, file), allow_pickle=True)

# for folder in next(os.walk(basePath))[1]:
#     print(folder)
#
#     for subfolder in next(os.walk(os.path.join(basePath, folder)))[1]:
#         print(subfolder)
#
# test = 5
