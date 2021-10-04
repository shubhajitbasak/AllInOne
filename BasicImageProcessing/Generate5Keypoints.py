import glob
import shutil

import cv2
import mediapipe as mp
import os

import cv2
import mediapipe as mp


def midpoint(p1, p2):
    coords = (p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0
    return coords


def relative_coord(shape, coord):
    x = coord[0]
    y = coord[1]
    relative_x = round(x * shape[1], 2)
    relative_y = round(y * shape[0], 2)
    return relative_x, relative_y


def generate5keypoints(img):
    mp_face_mesh = mp.solutions.face_mesh
    with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=2,
            min_detection_confidence=0.5) as face_mesh:
        # annotated_image = image.copy()
        results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.multi_face_landmarks is None or len(results.multi_face_landmarks) > 1:
            return None
        else:

            for face in results.multi_face_landmarks:
                shape = img.shape

                leftEye = relative_coord(shape, midpoint(face.landmark[33], face.landmark[133]))
                rightEye = relative_coord(shape, midpoint(face.landmark[362], face.landmark[263]))
                noseTip = relative_coord(shape, (face.landmark[1].x, face.landmark[1].y))
                mouthLeft = relative_coord(shape, (face.landmark[57].x, face.landmark[57].y))
                mouthRight = relative_coord(shape, (face.landmark[287].x, face.landmark[287].y))

                features = [leftEye, rightEye, noseTip, mouthLeft, mouthRight]
                return features


def main():
    rootDataPath = r'D:\codeProjects\Github\3DFace\data\CASIA-WebFace'

    imgPath = os.path.join(rootDataPath, 'images')
    # detectPath = os.path.join(rootDataPath, 'landmarks')

    # for root, dirs, files in os.walk(imgPath):
    #     if len(files) > 0:
    #         imgPath = root
    #         detectPath = root.replace('images', 'mask')
    #         if not len(glob.glob(imgPath + '/' + '*.jpg')) == len(glob.glob(detectPath + '/' + '*.jpg')):
    #             print(root)

    for root, dirs, files in os.walk(imgPath):
        if len(files) > 0 and not os.path.exists(root.replace('images', 'detections')):
            os.makedirs(root.replace('images', 'detections'), exist_ok=True)
            imgList = glob.glob(root + '/' + '*.jpg')
            print(root)

            for img in imgList:
                image = cv2.imread(img)
                ext = img.split('.')[-1]
                detectionPath = img.replace('images', 'detections').replace(ext, 'txt')
                if os.path.exists(detectionPath):
                    os.remove(detectionPath)
                lndmrks = generate5keypoints(image)
                if lndmrks is not None:
                    with open(detectionPath, "a") as f:  # img_addr.split('.')[0] + ".txt"
                        for i in lndmrks:
                            print(str(i[0]) + ' ' + str(i[1]), file=f)
                else:
                    # print('Issue : ', img)
                    os.remove(img)


if __name__ == "__main__":
    main()
