from vispy import app, scene
# from vispy.gloo.util import _screenshot
import numpy as np
# from moviepy.editor import VideoClip

canvas = scene.SceneCanvas(keys="interactive")
view = canvas.central_widget.add_view()
view.set_camera("turntable", mode="perspective", up="z", distance=2, azimuth=30, elevation=65)

xx, yy = np.arange(-1, 1, .02), np.arange(-1, 1, .02)
x, y = np.meshgrid(xx, yy)
r = np.sqrt(x**2+y**2)
z = lambda t: 0.1*np.sin(10*r-2*np.pi*t)
surface = scene.visuals.SurfacePlotVisual(x=xx-0.1, y=yy+0.2, z=z(0), shading="smooth", color=(0.5, 0.5, 1, 1))

view.add(surface)
canvas.show()