import pywavefront
import ctypes
import os

from pyglet.gl import *
from pywavefront import visualization, Wavefront

box1 = pywavefront.Wavefront(r'C:\Users\sbasak\Desktop\exp\IMG_0045_new.obj')

window = pyglet.window.Window(width=1280, height=720, resizable=True)

# root_path = os.path.dirname(__file__)

# box1 = Wavefront(os.path.join(root_path, 'data/box/box-V3F.obj'))


rotation = 0.0
lightfv = ctypes.c_float * 4


@window.event
def on_resize(width, height):
    viewport_width, viewport_height = window.get_framebuffer_size()
    glViewport(0, 0, viewport_width, viewport_height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., float(width)/height, 1., 100.)
    glMatrixMode(GL_MODELVIEW)
    return True


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))

    draw_box(box1, -4.0, 2.0)


def draw_box(box, x, y):
    glLoadIdentity()
    glTranslated(x, y, -10.0)
    # glRotatef(rotation, 0.0, 1.0, 0.0)
    # glRotatef(-25.0, 1.0, 0.0, 0.0)
    # glRotatef(45.0, 0.0, 0.0, 1.0)

    visualization.draw(box)


def update(dt):
    global rotation
    rotation += 90.0 * dt

    if rotation > 720.0:
        rotation = 0.0


pyglet.clock.schedule(update)
pyglet.app.run()