import numpy as np
from PIL import Image
from zipfile import ZipFile
# from keras.utils import Sequence
# from augment import BasicPolicy
import matplotlib.pyplot as plt
from io import BytesIO


def DepthNorm(depth_image, MaxDepth = 1000.0):
    return MaxDepth/depth_image


def extract_zip(input_zip):
    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def nyu_resize(img, resolution=480, padding=6):
    from skimage.transform import resize
    return resize(img, (resolution, int(resolution * 4 / 3)), preserve_range=True, mode='reflect', anti_aliasing=True)


MaxDepth = 1000.0


dictionary = extract_zip('data/data.zip')

nyu2_train = list(
        (row.split(',') for row in (dictionary['data/train.csv']).decode('utf-8').split('\r\n') if len(row) > 0)) #sbasak01
nyu2_test = list(
        (row.split(',') for row in (dictionary['data/test.csv']).decode('utf-8').split('\r\n') if len(row) > 0))

data = dictionary

for i in range(len(nyu2_train)):

    sample = nyu2_train[i]

    print(sample)
    # Read Images from list->bytes
    rgb_image = Image.open(BytesIO(data[sample[0]]))
    depth_image = Image.open(BytesIO(data[sample[1]]))

    # Reshape in dims
    rgb_image = np.asarray(rgb_image).reshape(480, 640, 3)
    depth_image = np.asarray(depth_image).reshape(480, 640, 1)

    # clip and norm
    rgb_image = np.clip(rgb_image / 255, 0, 1)
    depth_image = np.clip(depth_image / 255 * MaxDepth, 0, MaxDepth)
    depth_image_norm = DepthNorm(depth_image, MaxDepth)



# data1 = extract_zip(r'data/DataTest/our_Data.zip')
# data2 = extract_zip(r'data/DataTest/nyu_data_backup.zip')
# im11 = np.asarray(Image.open(BytesIO(data1['data/train/male/0002/Angry/rgb0023.png'])))
# im12 = np.asarray(Image.open(BytesIO(data1['data/train/male/0002/Angry/depth0023.png'])))
#
# im21 = np.asarray(Image.open(BytesIO(data2['data/nyu2_train/living_room_0038_out/167.jpg'])))
# im22 = np.asarray(Image.open(BytesIO(data2['data/nyu2_train/living_room_0038_out/167.png'])))
#
#
# x1 = np.clip(im11.reshape(480, 640, 3) / 255, 0, 1)
# y1 = np.clip(
#     im12.reshape(480, 640, 1) / 255 * maxDepth, 0,
#     maxDepth)
# y11 = DepthNorm(y1, maxDepth=maxDepth)
#
#
# x2 = np.clip(im21.reshape(480, 640, 3) / 255, 0, 1)
# y2 = np.clip(
#     im22.reshape(480, 640, 1) / 255 * maxDepth, 0,
#     maxDepth)
# y22 = DepthNorm(y2, maxDepth=maxDepth)
#
# plt.subplot(221), plt.imshow(x1)
# plt.subplot(222), plt.imshow(y1.squeeze())
#
# plt.subplot(223), plt.imshow(x2)
# plt.subplot(224), plt.imshow(y2.squeeze())
#
# plt.show()
#
#
# test = 'test'
