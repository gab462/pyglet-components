import pyglet
from pyglet.window import key
from scene import Scene
from components.triangle import TriangleComponent
from components.movement import MovementComponent
from entity import Entity


class Game(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.fps = 120

        self.keyboard = key.KeyStateHandler()
        self.push_handlers(self.keyboard)

    def run(self):
        self.set_main_scene()

        pyglet.clock.schedule_interval(self.update, 1/self.fps)

        pyglet.app.run()

    def set_main_scene(self):
        self.scene = Scene()

        ship = Entity(400, 300, size=30)

        ship.add_component(TriangleComponent(self.scene.batch, ship))
        ship.add_component(MovementComponent(self.keyboard, ship))

        self.scene.add_entity(ship)

    def on_draw(self):
        self.clear()
        self.scene.on_draw()

    def update(self, dt):
        self.scene.update(dt)


if __name__ == '__main__':
    Game().run()
