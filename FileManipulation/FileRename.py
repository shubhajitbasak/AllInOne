import os
import glob
import csv

# baseFemalePath = r"D:\project1\dataCreation\Data\female"
# baseMalePath = r"D:\project1\dataCreation\Data\male"

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


# for dir, subdirs, files in os.walk(baseMalePath):
#     for f in files:
#         if 'RGB' in f:
#             f_new = f.replace('RGB', 'rgb')
#             # print(os.path.join(dir, f), os.path.join(dir, f_new))
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
# for folder in next(os.walk(baseFileTestPathMale))[1]:
#     basePath = os.path.join(baseFileTestPathMale, folder)
#     # print(basePath)
#     for subfolder in next(os.walk(basePath))[1]:
#         baseTempPath = os.path.join(basePath, subfolder)
#         # depthExrCount = len(glob.glob1(baseTempPath, "depthExr*.exr"))
#         rgbCount = len(glob.glob1(baseTempPath, "rgb*.jpg"))
#         depthPngCount = len(glob.glob1(baseTempPath, "depth*.png"))
#         # dataFileCount = len(glob.glob1(baseTempPath, "data*.txt"))
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
