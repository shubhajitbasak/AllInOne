import numpy as np
import os

filePath = r'D:\Project2(2Dto3D)\Data\Now_Challenge\scanslmksonlypp\scans_lmks_onlypp'


def load_pp(fname):
    landmarks = np.zeros([7, 3]).astype(np.float32)
    with open(fname, 'r') as f:
        lines = f.readlines()
        for j in range(8, 15):
            line_contentes = lines[j].split(' ')
            # Check the .pp file to get to accurately pickup the columns for x , y and z coordinates
            for i in range(len(line_contentes)):
                if line_contentes[i].split('=')[0] == 'x':
                    x_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                elif line_contentes[i].split('=')[0] == 'y':
                    y_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                elif line_contentes[i].split('=')[0] == 'z':
                    z_content = float((line_contentes[i].split('=')[1]).split('"')[1])
                else:
                    pass
            landmarks[j - 8, :] = (np.array([x_content, y_content, z_content]).astype(np.float32))
    return landmarks


for dir, subdirs, files in os.walk(filePath):
    if len(files) > 0:
        for file in files:
            lmarks = load_pp(os.path.join(dir, file))


