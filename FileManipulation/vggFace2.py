import os
import cv2
import shutil

vggface2Path = '/mnt/sata/data/VGG-Face2/data'
with open(os.path.join(vggface2Path, 'test_list.txt')) as f1:
    list = f1.read().splitlines()

if os.path.exists(os.path.join(vggface2Path, 'test_list_mod.txt')):
    os.remove(os.path.join(vggface2Path, 'test_list_mod.txt'))

with open(os.path.join(vggface2Path, 'test_list_mod.txt'), 'w') as f2:
    for l in list:
        imgpath = os.path.join(vggface2Path, 'vggface2_test', 'test', l)
        img = cv2.imread(imgpath)
        if any([img.shape[0] < 224, img.shape[1] < 224]):
            print(img.shape)
        else:
            os.makedirs(os.path.join(vggface2Path, 'vggface2_test_mod', 'test', l.split('/')[0]), exist_ok=True)
            shutil.copy(imgpath, imgpath.replace('vggface2_test', 'vggface2_test_mod'))
            f2.write(imgpath + '\n')
