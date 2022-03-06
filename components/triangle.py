import pyglet
from math import sin, cos, pi

ONE_THIRD = 2 * pi / 3


def triangle_points(x, y, rotation, size):
    vertices = [0, ONE_THIRD, -ONE_THIRD]

    coord = lambda angle: (cos(angle + rotation) * size + x,
                           sin(angle + rotation) * size + y)

    coord_list = [coord(vertice) for vertice in vertices]

    return [point for coord in coord_list for point in coord]


class TriangleComponent:
    def __init__(self, batch, parent):
        self.parent = parent
        self.size = self.parent.size

        self.points = triangle_points(*self.parent.body.position,
                                      self.parent.body.rotation, self.size)
        self.shape = pyglet.shapes.Triangle(*self.points, batch=batch)

    def update(self, dt):
        self.points = triangle_points(*self.parent.body.position,
                                      self.parent.body.rotation, self.size)

        self.shape.position = self.points
