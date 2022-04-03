import numpy as np
from scipy.io import loadmat
import glob
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os


def draw_2d_landmarks(img, landmark, color='r', step=2):
    """
    Return:
        img              -- numpy.array, (B, H, W, 3) img with landmark, RGB order, range (0, 255)


    Parameters:
        img              -- numpy.array, (B, H, W, 3), RGB order, range (0, 255)
        landmark         -- numpy.array, (B, 68, 2), y direction is opposite to v direction
        color            -- str, 'r' or 'b' (red or blue)
    """
    if color == 'r':
        c = np.array([255, 0, 0])
    else:
        c = np.array([0, 0, 255])

    _, H, W, _ = img.shape
    img, landmark = img.copy(), landmark.copy()

    # lm_orig = landmark
    # landmark = landmark * (H / 224)
    landmark[..., 1] = H - 1 - landmark[..., 1]

    landmark = np.round(landmark).astype(np.int32)
    # img = np.round(img).astype(np.int32)
    for i in range(landmark.shape[1]):
        x, y = landmark[:, i, 0], landmark[:, i, 1]
        for j in range(-step, step):
            for k in range(-step, step):
                u = np.clip(x + j, 0, W - 1)
                v = np.clip(y + k, 0, H - 1)
                for m in range(landmark.shape[0]):
                    img[m, v[m], u[m]] = c
    plt.imshow(img[0])
    plt.show()
    return img


def plot_kpt(image, kpt):
    ''' Draw 68 key points
    Args:
        image: the input image
        kpt: (68, 3).
    '''

    end_list = np.array([17, 22, 27, 42, 48, 31, 36, 68], dtype=np.int32) - 1

    image = image.copy()
    kpt = np.round(kpt).astype(np.int32)
    for i in range(kpt.shape[0]):
        st = kpt[i, :2]
        image = cv2.circle(image, (st[0], st[1]), 1, (0, 0, 255), 2)
        if i in end_list:
            continue
        ed = kpt[i + 1, :2]
        image = cv2.line(image, (st[0], st[1]), (ed[0], ed[1]), (255, 255, 255), 1)
    return image


# list = glob.glob('/mnt/sata/code/myGit/3DFace/datasets/examples/*.jpg')
#
# for imgf in list:
#     img = cv2.imread(imgf)
#     # img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # img = img.reshape(1, img.shape[0], img.shape[1], 3)
#     gtmatfile = imgf.replace('.jpg', '_GT.mat')
#     predmatfile = imgf.replace('.jpg', '.mat')
#     lmGt = loadmat(gtmatfile)['pt3d_68']
#     lmGt = lmGt.reshape(68, 3)
#     # draw = draw_2d_landmarks(img, lmGt)
#     lmPred = loadmat(predmatfile)['lm68']
#     # draw = draw_2d_landmarks(img, lmGt)
#     plt.imshow(img)
#     plt.show()
#     print('test')
#
# print('test')

# img1 = Image.open('/mnt/sata/data/AFLW2000-3D/AFLW2000/image00002.jpg')
# img1RGB = img1.convert('RGB')
# print(img1.getpixel((216, 312)))


# list = glob.glob('/mnt/sata/code/myGit/3DFace/datasets/examples/*.jpg')
# outdir = '/mnt/sata/code/myGit/3DFace/datasets/examples/out/'
#
# for imgf in list:
#
#     gtmatfile = imgf.replace('.jpg', '_GT.mat')
#     predmatfile = imgf.replace('.jpg', '.mat')
#
#     img = cv2.imread(imgf)
#     lmGt = loadmat(gtmatfile)['pt3d_68']
#     # lmGt = lmGt * (224/img.shape[1])
#     # lmGt_T = lmGt.transpose()[:, 0:2]
#     # lmPred = loadmat(predmatfile)['lm68']
#     img = img.copy()
#     # img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
#
#     # cv2.imwrite(os.path.join(outdir, imgf.split('/')[-1]), img)
#     # np.save(os.path.join(outdir, imgf.split('/')[-1].replace('.jpg','.npy')), lmGt_T)
#
#     c = np.array([255, 0, 0])
#     step = 1
#     for i in range(lmGt.shape[1]):
#         for x, y in zip(lmGt[1,:], lmGt[0,:]):
#             x1 = np.round(x).astype(np.int32)
#             y1 = np.round(y).astype(np.int32)
#             for j in range(-step, step + 1):
#                 for k in range(-step, step + 1):
#                     img[x1 + j, y1 + k] = c
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     plt.imshow(imgRGB)
#     plt.show()


list = glob.glob('/mnt/sata/code/myGit/3DFace/datasets/examples/out/*.png')
for f in list:
    img = cv2.imread(f)
    lmPred = loadmat(f.replace('.png','.mat'))['lm68'][0]
    # lmPred = np.load('/mnt/sata/code/myGit/3DFace/datasets/examples/out/image04276.npy')
    # img = img1.copy()
    # img = cv2.resize(img1, (224,224), interpolation=cv2.INTER_AREA)
    c = np.array([255, 0, 0])
    step = 1
    for i in range(lmPred.shape[0]):
        for x, y in zip(lmPred[:,1], lmPred[:,0]):
            x1 = np.round(x).astype(np.int32)
            y1 = np.round(y).astype(np.int32)
            img[x1, y1] = c
            for j in range(-step, step + 1):
                for k in range(-step, step + 1):
                    # print(x + j, y + k)
                    img[x1 + j, y1 + k] = c

    lmGT = np.load(f.replace('.png','.npy'))
    # img = img1.copy()
    # img = cv2.resize(img1, (224,224), interpolation=cv2.INTER_AREA)
    c = np.array([0, 0, 255])
    step = 1
    for i in range(lmGT.shape[0]):
        for x, y in zip(lmGT[:,1], lmGT[:,0]):
            x1 = np.round(x).astype(np.int32)
            y1 = np.round(y).astype(np.int32)
            img[x1, y1] = c
            for j in range(-step, step + 1):
                for k in range(-step, step + 1):
                    # print(x + j, y + k)
                    img[x1 + j, y1 + k] = c

    # img = cv2.resize(img, (224,224), interpolation=cv2.INTER_AREA)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imsave(f.replace('.png','_kp.png'), imgRGB)
    # plt.imshow(imgRGB)
    # plt.show()