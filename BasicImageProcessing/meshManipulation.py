import pymesh


def convertrgbObj2Obj(objPath, newPath):
    with open(objPath) as f:
        lines = f.readlines()
        newlines = []
        for line in lines:
            if line.startswith('v'):
                newlines.append(' '.join(line.split(' ')[:-3]) + '\n')
            # print(line)
            else:
                newlines.append(line)

    with open(newPath, 'w') as f1:
        for item in newlines:
            f1.write("%s" % item)


convertrgbObj2Obj(r'C:\Users\sbasak\Desktop\exp\IMG_0045.obj',
                  r'C:\Users\sbasak\Desktop\exp\IMG_0045_new.obj')
