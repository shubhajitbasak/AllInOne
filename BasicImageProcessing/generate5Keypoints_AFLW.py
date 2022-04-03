import cv2
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
import os


def gen5keyponitsAFLW(lm):
    leftEye = (lm[36] + lm[39]) / 2
    rightEye = (lm[42] + lm[45]) / 2
    noseTip = lm[30]
    mouthLeft = lm[48]
    mouthRight = lm[54]
    features = [leftEye, rightEye, noseTip, mouthLeft, mouthRight]
    features = np.asarray(features)
    return features


# load landmarks for standard face, which is used for image preprocessing
def load_lm3d():
    Lm3D = loadmat('/mnt/sata/code/myGit/AllInOne/HelperFiles/similarity_Lm3D_all.mat')
    Lm3D = Lm3D['lm']

    # calculate 5 facial landmarks using 68 landmarks
    lm_idx = np.array([31, 37, 40, 43, 46, 49, 55]) - 1
    Lm3D = np.stack([Lm3D[lm_idx[0], :], np.mean(Lm3D[lm_idx[[1, 2]], :], 0), np.mean(
        Lm3D[lm_idx[[3, 4]], :], 0), Lm3D[lm_idx[5], :], Lm3D[lm_idx[6], :]], axis=0)
    Lm3D = Lm3D[[1, 2, 0, 3, 4], :]

    return Lm3D


# calculating least square problem for image alignment
def POS(xp, x):
    npts = xp.shape[1]

    A = np.zeros([2 * npts, 8])

    A[0:2 * npts - 1:2, 0:3] = x.transpose()
    A[0:2 * npts - 1:2, 3] = 1

    A[1:2 * npts:2, 4:7] = x.transpose()
    A[1:2 * npts:2, 7] = 1

    b = np.reshape(xp.transpose(), [2 * npts, 1])

    k, _, _, _ = np.linalg.lstsq(A, b)

    R1 = k[0:3]
    R2 = k[4:7]
    sTx = k[3]
    sTy = k[7]
    s = (np.linalg.norm(R1) + np.linalg.norm(R2)) / 2
    t = np.stack([sTx, sTy], axis=0)

    return t, s


# resize and crop images for face reconstruction
def resize_n_crop_img(img, lm, t, s, target_size=224.):
    w0, h0 = img.size
    w = (w0 * s).astype(np.int32)
    h = (h0 * s).astype(np.int32)
    left = (w / 2 - target_size / 2 + float((t[0] - w0 / 2) * s)).astype(np.int32)
    right = left + target_size
    up = (h / 2 - target_size / 2 + float((h0 / 2 - t[1]) * s)).astype(np.int32)
    below = up + target_size

    img = img.resize((w, h), resample=Image.BICUBIC)
    img = img.crop((left, up, right, below))

    lm = np.stack([lm[:, 0] - t[0] + w0 / 2, lm[:, 1] -
                   t[1] + h0 / 2], axis=1) * s
    lm = lm - np.reshape(
        np.array([(w / 2 - target_size / 2), (h / 2 - target_size / 2)]), [1, 2])

    return img, lm


def align_img(img, lm, lm3D, target_size=224., rescale_factor=102.):
    """
    Return:
        transparams        --numpy.array  (raw_W, raw_H, scale, tx, ty)
        img_new            --PIL.Image  (target_size, target_size, 3)
        lm_new             --numpy.array  (68, 2), y direction is opposite to v direction
        mask_new           --PIL.Image  (target_size, target_size)

    Parameters:
        img                --PIL.Image  (raw_H, raw_W, 3)
        lm                 --numpy.array  (68, 2), y direction is opposite to v direction
        lm3D               --numpy.array  (5, 3)
        mask               --PIL.Image  (raw_H, raw_W, 3)
    """

    w0, h0 = img.size
    lm5p = gen5keyponitsAFLW(lm)

    # calculate translation and scale factors using 5 facial landmarks and standard landmarks of a 3D face
    t, s = POS(lm5p.transpose(), lm3D.transpose())
    s = rescale_factor / s

    # processing the image
    img_new, lm_new = resize_n_crop_img(img, lm, t, s, target_size=target_size)
    trans_params = np.array([w0, h0, s, t[0], t[1]])

    return trans_params, img_new, lm_new


list = glob.glob('/mnt/sata/code/myGit/3DFace/datasets/examples/*.jpg')
outdir = '/mnt/sata/code/myGit/3DFace/datasets/examples/out/'

for imgf in list:
    imgName = imgf.split('/')[-1]
    gtmatfile = imgf.replace('.jpg', '_GT.mat')
    # img = cv2.imread('/mnt/sata/code/myGit/3DFace/datasets/examples/tmp1/image04276.jpg')
    img = Image.open(imgf)
    lmGt = loadmat(gtmatfile)['pt3d_68']
    lmGt_T = lmGt.transpose()[:, 0:2]

    lm5p = gen5keyponitsAFLW(lmGt_T)

    lm3d = load_lm3d()

    _, img, lms = align_img(img, lmGt_T, lm3d)
    np.save(os.path.join(outdir,imgName.replace('.jpg', '.npy')), lms)
    np.save(os.path.join(outdir, imgName.replace('.jpg', '_5kp.npy')), lm5p)


print('test')
# c = np.array([255, 0, 0])
# step = 1
# for f in fets:
#     x1 = np.round(f[1]).astype(np.int32)
#     y1 = np.round(f[0]).astype(np.int32)
#     for j in range(-step, step + 1):
#         for k in range(-step, step + 1):
#             img[x1 + j, y1 + k] = c
# imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(imgRGB)
# plt.show()
