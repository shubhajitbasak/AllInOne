import os
import glob
import shutil

i = 0

for root, dirs, files in os.walk(r'C:\Users\sbasak\Downloads\lfw\lfw'):
    if len(files) > 0:
        imgList = glob.glob(root + '/' + '*.jpg')

        for img in imgList:
            shutil.copy(img, r'D:\Project2(2Dto3D)\Data\lfw\Images'+'\lfw_'+str(i) + '.jpg')
            i = i+1


#******************************************************************

import os
import string
import glob
from shutil import copyfile
import pathlib

# baseFemalePath = r"D:\project1\dataCreation\Data\female"
# baseMalePath = r"D:\project1\dataCreation\Data\male"
# logFile = r"D:\project1\dataCreation\Data\dataCheck.log"
#
# if os.path.exists(logFile):
#     os.remove(logFile)
#
# f = open(logFile, "a")
#
# # print(next(os.walk(baseFemalePath))[1])
# #
# # print(os.path.join(baseFemalePath,next(os.walk(baseFemalePath))[1][0]))
#
#
# # Check all the folders has ['Angry', 'Happy', 'Neutral', 'Sad', 'Scared']
#
# f.write(" ----------- Female Folder Check Start ----------- ")
#
# for folder in next(os.walk(baseFemalePath))[1]:
#     # print(folder)
#     basePath = os.path.join(baseFemalePath, folder)
#     # print(basePath)
#     # print(next(os.walk(basePath))[1])
#     if next(os.walk(basePath))[1] != ['Angry', 'Happy', 'Neutral', 'Sad', 'Scared']:
#         f.write("\n \n Folder Missing in --- {0}".format(basePath))
#
#     for subfolder in next(os.walk(basePath))[1]:
#         baseTempPath = os.path.join(basePath, subfolder)
#         # print(baseTempPath)
#         f.write("\n Folder : {0} -------- EXR Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "depthExr*.exr"))))
#
#         f.write(" \n Folder : {0} -------- RGB Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "rgb*.png"))))
#
#         f.write(" \n Folder : {0} -------- DEPTH Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "depth*.png"))))
#
#         f.write(" \n Folder : {0} -------- DEPTH Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "data*.txt"))))
#
#         f.write("\n")
#
# f.write("\n \n ----------- Female Folder Check End -----------")
#
# f.write(" \n \n ----------- Male Folder Check Start -----------")
#
# for folder in next(os.walk(baseMalePath))[1]:
#     # print(folder)
#     basePath = os.path.join(baseMalePath, folder)
#     # print(basePath)
#     # print(next(os.walk(basePath))[1])
#     if next(os.walk(basePath))[1] != ['Angry', 'Happy', 'Neutral', 'Sad', 'Scared']:
#         f.write("Folder Missing in --- {0}".format(basePath))
#
#     for subfolder in next(os.walk(basePath))[1]:
#         baseTempPath = os.path.join(basePath, subfolder)
#         # print(baseTempPath)
#         f.write("\n Folder : {0} -------- EXR Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "depthExr*.exr"))))
#
#         f.write(" \n Folder : {0} -------- RGB Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "rgb*.png"))))
#
#         f.write(" \n Folder : {0} -------- DEPTH Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "depth*.png"))))
#
#         f.write(" \n Folder : {0} -------- DEPTH Count : {1}".format(baseTempPath, len(glob.glob1(baseTempPath, "data*.txt"))))
#
#         f.write("\n")
#
# f.write(" \n \n ----------- Male Folder Check Ends -----------")
#
# f.close()


traincsvFilepath = r'C:\project1\dataCreation\Data\data_train.csv'  # 'data_exr/data_train.csv'
testcsvFilepath = r'C:\project1\dataCreation\Data\data_test.csv'  # 'data_exr/data_test.csv'

with open(traincsvFilepath, 'r') as f:
    x = [line.rstrip() for line in f]

my_train_list = list((row.split(',') for row in x if len(row) > 0))

with open(testcsvFilepath, 'r') as f:
    y = [line.rstrip() for line in f]
my_test_list = list((row.split(',') for row in y if len(row) > 0))

# testing
if True:
    # testCount = int(trainCount/5)
    my_train_list = my_train_list[0:400]
    my_test_list = my_test_list[0:100]

basePath = r'C:\project1\dataCreation\DataTest'

for t in my_test_list:
    print(t[0], t[1])
    # print(os.path.join(basePath,'\\'.join(t[0].split('\\')[4:])))

    t0 = os.path.join(basePath,'\\'.join(t[0].split('\\')[4:]))
    t1 = os.path.join(basePath,'\\'.join(t[1].split('\\')[4:]))
    baseTempPath = os.path.join(basePath,'\\'.join(t[0].split('\\')[4:-1]))
    print(t0, t1)
    print(baseTempPath)

    if not os.path.exists(baseTempPath):
        pathlib.Path(baseTempPath).mkdir(parents=True, exist_ok=True)

    copyfile(t[0],t0)
    copyfile(t[1],t1)


