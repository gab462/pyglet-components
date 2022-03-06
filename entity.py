import pymunk


class Entity:
    def __init__(self, x, y, rotation = 0, size = 1, elasticity = 1, density = 1):
        self.size = size
        self.components = []

        self.body = pymunk.Body()
        self.body.position = (x, y)
        self.body.rotation = rotation

        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.elasticity = elasticity
        self.shape.density = density

    def add_component(self, component):
        self.components.append(component)

    def set_velocity(self, velocity):
        self.body.velocity = velocity

    def update(self, dt):
        for component in self.components:
            component.update(dt)
