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


