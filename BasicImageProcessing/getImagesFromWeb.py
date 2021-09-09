import requests
import shutil
import os
with open(r'D:\Project2(2Dto3D)\Data\faceScrub\facescrub_actresses.txt') as f:
    lines = f.readlines()[1:]
urls = []
i = 60000
for line in lines:

    # urls.append(line.split('\t')[3])
    # image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"
    image_url = line.split('\t')[3]
    filename = image_url.split("/")[-1]

    fileSaveName = 'facescrub_'+str(i) + '.' + filename.split('.')[-1]

    try:

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(image_url, stream=True, verify=False, timeout=10)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(os.path.join(r'D:\Project2(2Dto3D)\Data\faceScrub\Images', fileSaveName), 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')

    except:
        print('Image Couldn\'t be retreived')

    i = i+1
