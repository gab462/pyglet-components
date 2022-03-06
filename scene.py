import pyglet
import pymunk


class Scene:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.entities = []

        self.space = pymunk.Space()

    def add_entity(self, entity):
        self.entities.append(entity)
        self.space.add(entity.body, entity.shape)

    def on_draw(self):
        self.batch.draw()

    def set_gravity(self, gravity):
        self.space.gravity = gravity

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)

        self.space.step(dt)
