import numpy as np

from screen import Screen
from mesh import Mesh
from camera import OrthoCamera
from renderer import Renderer

import numpy as np

if __name__ == '__main__':
    screen = Screen(500, 500)

    camera = OrthoCamera(-1, 1, -1, 1, 0.5, 100)
    camera.transform.set_position(0, -15, 0)

    mesh = Mesh.from_stl("suzanne.stl", None, None, 0, 0, 0, 0)
    # mesh.transform.set_rotation(-15, 0, 45)

    renderer = Renderer(screen, camera, mesh, None)
    renderer.render("depth", [100, 50, 50], [0, 0, 0])

    screen.show()
