# https://github.com/deepinsight/insightface
# https://github.com/deepinsight/insightface/tree/master/python-package
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
import glob

app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(224, 224))
# img = cv2.imread('samples/1.jpg')
# faces = app.get(img)
# rimg = app.draw_on(img, faces)
# cv2.imwrite("./t1_output.jpg", rimg)


imgList = glob.glob('/mnt/sata/code/myGit/3DFace/datasets/examples/*.jpg')
for img in imgList:
    image = cv2.imread(img)
    faces = app.get(image)
    ext = img.split('.')[-1]
    detectionPath = img.replace('examples', 'examples/detections').replace(ext, 'txt')
    if len(faces) > 0:
        lndmrks = faces[0]['kps']
        with open(detectionPath, "a") as f:
            for i in lndmrks:
                print(str(i[0]) + ' ' + str(i[1]), file=f)
    # if os.path.exists(detectionPath):
    #     os.remove(detectionPath)
    # lndmrks = generate5keypoints(image)
    # if lndmrks is not None:
    #     with open(detectionPath, "a") as f:  # img_addr.split('.')[0] + ".txt"
    #         for i in lndmrks:
    #             print(str(i[0]) + ' ' + str(i[1]), file=f)
    #     finalimglist.append(img)
    # else:
    #     # print('Issue : ', img)
    #     os.remove(img)