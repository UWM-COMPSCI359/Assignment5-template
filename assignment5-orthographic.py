import numpy as np

from mesh import Mesh
from camera import OrthoCamera
from screen import Screen
from renderer import Renderer
from light import PointLight

if __name__ == '__main__':
    screen = Screen(500, 500)

    camera = OrthoCamera(-1, 1, -1, 1, 1, 100)
    camera.transform.set_position(0, -5, 0)

    light = PointLight(100.0, np.array([1, 1, 1]))
    light.transform.set_position(0, -5, 5)

    diffuse_color = np.array([1.0, 0.0, 0.7])
    specular_color = np.array([1.0, 1.0, 1.0])
    kd = 1.0
    ks = 0.25
    ka = 0.2
    p = 50
    mesh = Mesh.from_stl("unit_sphere.stl", diffuse_color, specular_color, ka, kd, ks, p)

    renderer = Renderer(screen, camera, mesh, light)
    renderer.render("flat", np.array([80,80,80]), np.array([0.2, 0.2, 0.2]))

    screen.show()

