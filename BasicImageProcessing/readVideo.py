import ffmpeg

import imageio

reader = imageio.get_reader('imageio:Indoor-Cooperative.mjpg')


stream = ffmpeg.input(r'C:\Users\sbasak\Downloads\FlorenceFace\Florence\subject_01\Video\Indoor-Cooperative.mjpg')

stream = ffmpeg.output(stream, r'C:\Users\sbasak\Desktop\thumbs\test-%d.jpg',
        start_number=0)

ffmpeg.run(stream)

test = 5