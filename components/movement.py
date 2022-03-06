from pyglet.window import key
from math import sin, cos


class MovementComponent:
    def __init__(self, keyboard, parent, force = 10 ** 6, rotate_amount = 5):
        self.parent = parent
        self.keyboard = keyboard
        self.force = force
        self.rotate_amount = rotate_amount

    def update(self, dt):
        if self.keyboard[key.W]:
            self.parent.body.apply_impulse_at_local_point((self.force * cos(self.parent.body.rotation) * dt,
                                                           self.force * sin(self.parent.body.rotation) * dt))

        if self.keyboard[key.A]:
            self.parent.body.rotation += dt * self.rotate_amount

        if self.keyboard[key.D]:
            self.parent.body.rotation -= dt * self.rotate_amount
