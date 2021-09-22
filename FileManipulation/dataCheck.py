import glob
import os
import shutil

rootPath = r'D:\Project2(2Dto3D)\Code\Deep3DFaceRecon_pytorch\datasets\facescrub'

imgList_jpg = glob.glob1(rootPath, '*.jpg')
imgList_png = glob.glob1(rootPath, '*.png')

imgList = sorted(imgList_jpg + imgList_png)
detectionList = glob.glob1(os.path.join(rootPath,'detections'), '*.txt')

print(len(imgList))
print(len(detectionList))

for img in imgList:

    detectionPath = os.path.join(rootPath, 'detections', img.split('.')[0] + '.txt')
    if not os.path.exists(detectionPath):
        print(os.path.join(rootPath, img))
        # shutil.move(os.path.join(rootPath, img), os.path.join(rootPath, 'Issues', img))

# detectionList = sorted(glob.glob1(os.path.join(rootPath, 'detections'), '*.txt'))
#
#
# for img, txt in zip(imgList, detectionList):
#     if not img.split('.')[0] == txt.split('.')[0]:
#         print('error in : ' + str(img))
