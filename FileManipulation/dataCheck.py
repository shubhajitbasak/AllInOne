
import glob
import os

rootPath = r'D:\Project2(2Dto3D)\Data\FaceScrub'

imgList_jpg = glob.glob1(rootPath, '*.jpg')
imgList_png = glob.glob1(rootPath, '*.png')

imgList = sorted(imgList_jpg + imgList_png)

detectionList = sorted(glob.glob1(os.path.join(rootPath, 'detections'), '*.txt'))


for img, txt in zip(imgList, detectionList):
    if not img.split('.')[0] == txt.split('.')[0]:
        print('error in : ' + str(img))


