# -*- coding: utf-8 -*-
# vispy: gallery 2
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

#
# Modified for animation with MoviePy by Zulko
# See result here: http://i.imgur.com/sSCBkFd.gif
#

"""
3D brain mesh viewer.
"""

from timeit import default_timer
import numpy as np

from vispy import gloo
from vispy import app
from vispy.util.transforms import perspective, translate, rotate
from vispy.io import load_data_file
from vispy.gloo.util import _screenshot

brain = np.load(load_data_file('brain/brain.npz', force_download='2014-09-04'))
data = brain['vertex_buffer']
faces = brain['index_buffer']

VERT_SHADER = """
#version 120
uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_projection;
uniform vec4 u_color;
attribute vec3 a_position;
attribute vec3 a_normal;
attribute vec4 a_color;
varying vec3 v_position;
varying vec3 v_normal;
varying vec4 v_color;
void main()
{
    v_normal = a_normal;
    v_position = a_position;
    v_color = a_color * u_color;
    gl_Position = u_projection * u_view * u_model * vec4(a_position,1.0);
}
"""

FRAG_SHADER = """
#version 120
uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_normal;
uniform vec3 u_light_intensity;
uniform vec3 u_light_position;
varying vec3 v_position;
varying vec3 v_normal;
varying vec4 v_color;
void main()
{
    // Calculate normal in world coordinates
    vec3 normal = normalize(u_normal * vec4(v_normal,1.0)).xyz;
    // Calculate the location of this fragment (pixel) in world coordinates
    vec3 position = vec3(u_view*u_model * vec4(v_position, 1));
    // Calculate the vector from this pixels surface to the light source
    vec3 surfaceToLight = u_light_position - position;
    // Calculate the cosine of the angle of incidence (brightness)
    float brightness = dot(normal, surfaceToLight) /
                      (length(surfaceToLight) * length(normal));
    brightness = max(min(brightness,1.0),0.0);
    // Calculate final color of the pixel, based on:
    // 1. The angle of incidence: brightness
    // 2. The color/intensities of the light: light.intensities
    // 3. The texture and texture coord: texture(tex, fragTexCoord)
    // Specular lighting.
    vec3 surfaceToCamera = vec3(0.0, 0.0, 1.0) - position;
    vec3 K = normalize(normalize(surfaceToLight) + normalize(surfaceToCamera));
    float specular = clamp(pow(abs(dot(normal, K)), 40.), 0.0, 1.0);

    gl_FragColor = v_color * brightness * vec4(u_light_intensity, 1);
}
"""


class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive')
        self.size = 400, 300

        self.program = gloo.Program(VERT_SHADER, FRAG_SHADER)

        self.theta, self.phi = -80, 180
        self.translate = 2.5

        self.faces = gloo.IndexBuffer(faces)
        self.program.bind(gloo.VertexBuffer(data))

        self.program['u_color'] = 1, 1, 1, 1
        self.program['u_light_position'] = (1., 1., 1.)
        self.program['u_light_intensity'] = (1., 1., 1.)

        gloo.set_state(blend=False, depth_test=True, polygon_offset_fill=True)
        self.update_matrices()

    def update_matrices(self):
        self.view = np.eye(4, dtype=np.float32)
        self.model = np.eye(4, dtype=np.float32)
        self.projection = np.eye(4, dtype=np.float32)

        rotate(self.model, self.theta, 1, 0, 0)
        rotate(self.model, self.phi, 0, 1, 0)
        translate(self.view, 0, 0, -self.translate)

        self.program['u_model'] = self.model
        self.program['u_view'] = self.view
        self.program['u_normal'] = np.array(np.matrix(np.dot(self.view,
                                                             self.model)).I.T)

    def on_resize(self, event):
        width, height = event.size
        gloo.set_viewport(0, 0, width, height)
        self.projection = perspective(45.0, width / float(height), 1.0, 20.0)
        self.program['u_projection'] = self.projection

    def animation(self, t):
        """ Added for animation with MoviePy """
        self.phi, self.theta = 180 * t, -80
        self.update_matrices()
        self.update()
        gloo.clear()
        self.program.draw('triangles', indices=self.faces)
        return _screenshot((0, 0, self.size[0], self.size[1]))[:, :, :3]


def expample1():
    from moviepy.editor import VideoClip

    canvas = Canvas()
    canvas.show()
    clip = VideoClip(canvas.animation, duration=2)
    clip.write_videofile('brain.mp4', fps=20)
    # clip.write_gif('brain.gif', fps=20, opt='OptimizePlus', fuzz=10)


"""
This example shows how to display 3D objects.
You should see a colored outlined spinning cube.
"""

import numpy as np
from vispy import app, gloo
from vispy.util.transforms import perspective, translate, rotate

vert = """
// Uniforms
// ------------------------------------
uniform   mat4 u_model;
uniform   mat4 u_view;
uniform   mat4 u_projection;
uniform   vec4 u_color;
// Attributes
// ------------------------------------
attribute vec3 a_position;
attribute vec4 a_color;
attribute vec3 a_normal;
// Varying
// ------------------------------------
varying vec4 v_color;
void main()
{
    v_color = a_color * u_color;
    gl_Position = u_projection * u_view * u_model * vec4(a_position,1.0);
}
"""


frag = """
// Varying
// ------------------------------------
varying vec4 v_color;
void main()
{
    gl_FragColor = v_color;
}
"""


# -----------------------------------------------------------------------------
def cube():
    """
    Build vertices for a colored cube.
    V  is the vertices
    I1 is the indices for a filled cube (use with GL_TRIANGLES)
    I2 is the indices for an outline cube (use with GL_LINES)
    """
    vtype = [('a_position', np.float32, 3),
             ('a_normal', np.float32, 3),
             ('a_color', np.float32, 4)]
    # Vertices positions
    v = [[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1],
         [1, -1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, -1]]
    # Face Normals
    n = [[0, 0, 1], [1, 0, 0], [0, 1, 0],
         [-1, 0, 1], [0, -1, 0], [0, 0, -1]]
    # Vertice colors
    c = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 1],
         [1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]]

    V = np.array([(v[0], n[0], c[0]), (v[1], n[0], c[1]),
                  (v[2], n[0], c[2]), (v[3], n[0], c[3]),
                  (v[0], n[1], c[0]), (v[3], n[1], c[3]),
                  (v[4], n[1], c[4]), (v[5], n[1], c[5]),
                  (v[0], n[2], c[0]), (v[5], n[2], c[5]),
                  (v[6], n[2], c[6]), (v[1], n[2], c[1]),
                  (v[1], n[3], c[1]), (v[6], n[3], c[6]),
                  (v[7], n[3], c[7]), (v[2], n[3], c[2]),
                  (v[7], n[4], c[7]), (v[4], n[4], c[4]),
                  (v[3], n[4], c[3]), (v[2], n[4], c[2]),
                  (v[4], n[5], c[4]), (v[7], n[5], c[7]),
                  (v[6], n[5], c[6]), (v[5], n[5], c[5])],
                 dtype=vtype)
    I1 = np.resize(np.array([0, 1, 2, 0, 2, 3], dtype=np.uint32), 6 * (2 * 3))
    I1 += np.repeat(4 * np.arange(2 * 3, dtype=np.uint32), 6)

    I2 = np.resize(
        np.array([0, 1, 1, 2, 2, 3, 3, 0], dtype=np.uint32), 6 * (2 * 4))
    I2 += np.repeat(4 * np.arange(6, dtype=np.uint32), 8)

    return V, I1, I2


# -----------------------------------------------------------------------------
class Canvas(app.Canvas):

    def __init__(self):
        app.Canvas.__init__(self, keys='interactive', size=(800, 600))

        self.vertices, self.filled, self.outline = cube()
        self.filled_buf = gloo.IndexBuffer(self.filled)
        self.outline_buf = gloo.IndexBuffer(self.outline)

        self.program = gloo.Program(vert, frag)
        self.program.bind(gloo.VertexBuffer(self.vertices))

        self.view = translate((0, 0, -5))
        self.model = np.eye(4, dtype=np.float32)

        gloo.set_viewport(0, 0, self.physical_size[0], self.physical_size[1])
        self.projection = perspective(45.0, self.size[0] /
                                      float(self.size[1]), 2.0, 10.0)

        self.program['u_projection'] = self.projection

        self.program['u_model'] = self.model
        self.program['u_view'] = self.view

        self.theta = 0
        self.phi = 0

        gloo.set_clear_color('white')
        gloo.set_state('opaque')
        gloo.set_polygon_offset(1, 1)

        self._timer = app.Timer('auto', connect=self.on_timer, start=True)

        self.show()

    # ---------------------------------
    def on_timer(self, event):
        self.theta += .5
        self.phi += .5
        self.model = np.dot(rotate(self.theta, (0, 1, 0)),
                            rotate(self.phi, (0, 0, 1)))
        self.program['u_model'] = self.model
        self.update()

    # ---------------------------------
    def on_resize(self, event):
        gloo.set_viewport(0, 0, event.physical_size[0], event.physical_size[1])
        self.projection = perspective(45.0, event.size[0] /
                                      float(event.size[1]), 2.0, 10.0)
        self.program['u_projection'] = self.projection

    # ---------------------------------
    def on_draw(self, event):
        gloo.clear()

        # Filled cube

        gloo.set_state(blend=False, depth_test=True, polygon_offset_fill=True)
        self.program['u_color'] = 1, 1, 1, 1
        self.program.draw('triangles', self.filled_buf)

        # Outline
        gloo.set_state(blend=True, depth_test=True, polygon_offset_fill=False)
        gloo.set_depth_mask(False)
        self.program['u_color'] = 0, 0, 0, 1
        self.program.draw('lines', self.outline_buf)
        gloo.set_depth_mask(True)


# -----------------------------------------------------------------------------
def expample2():
    c = Canvas()
    app.run()

if __name__ == '__main__':
    expample2()