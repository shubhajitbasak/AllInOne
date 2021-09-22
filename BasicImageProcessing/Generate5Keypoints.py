import glob
import shutil

import cv2
import mediapipe as mp
import os


def midpoint(p1, p2):
    coords = (p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0
    return coords


def relative_coord(shape, coord):
    x = coord[0]
    y = coord[1]
    relative_x = round(x * shape[1], 2)
    relative_y = round(y * shape[0], 2)
    return relative_x, relative_y


mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

image_path = r'C:\Users\sbasak\Desktop\exp\now_sample'
landmark_path_root = r'C:\Users\sbasak\Desktop\exp\now_sample\detections'

img_list_jpg = sorted(glob.glob(image_path + '/' + '*.jpg'))

img_list_png = sorted(glob.glob(image_path + '/' + '*.png'))

img_list = img_list_jpg + img_list_png

print(len(img_list))

# l = 0

for img_addr in img_list:
    # l = l + 1

    image = cv2.imread(img_addr)
    # image = cv2.imread(r'D:\Project2(2Dto3D)\Data\lfw\Images\lfw_10136.jpg')
    # image = cv2.imread('/mnt/fastssd/Shubhajit_Stuff/2dTo3d/Deep3DFaceReconstruction/input/000063.jpg')

    # drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    if not image is None:
        with mp_face_mesh.FaceMesh(
                static_image_mode=True,
                max_num_faces=2,
                min_detection_confidence=0.5) as face_mesh:
            # annotated_image = image.copy()
            results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # if not results.multi_face_landmarks is None:
            #     s = 1
            #     # print(img_addr, len(results.multi_face_landmarks))
            # else:
            #     shutil.move(img_addr, img_addr.replace('/input/', '/input_reject/'))
            #     print(img_addr, 'None')

            landmark_path = os.path.join(landmark_path_root, img_addr.split('\\')[-1].split('.')[0] + '.txt')

            print(img_addr)

            if results.multi_face_landmarks == None or len(results.multi_face_landmarks) > 1:
                shutil.move(img_addr, img_addr.replace('Images', 'Images_multiple'))
            else:

                for face in results.multi_face_landmarks:

                    shape = image.shape

                    leftEye = relative_coord(shape, midpoint(face.landmark[33], face.landmark[133]))
                    rightEye = relative_coord(shape, midpoint(face.landmark[362], face.landmark[263]))
                    noseTip = relative_coord(shape, (face.landmark[1].x, face.landmark[1].y))
                    mouthLeft = relative_coord(shape, (face.landmark[57].x, face.landmark[57].y))
                    mouthRight = relative_coord(shape, (face.landmark[287].x, face.landmark[287].y))

                    features = [leftEye, rightEye, noseTip, mouthLeft, mouthRight]
                    with open(landmark_path, "a") as f:  # img_addr.split('.')[0] + ".txt"
                        for i in features:
                            print(str(i[0]) + ' ' + str(i[1]), file=f)
    else:
        shutil.move(img_addr, img_addr.replace('Images', 'Images_multiple'))

# print('l : ', l)
