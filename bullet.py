from sprite import *
from math import *
from collider import *
from all_various import *


class Bullet(Sprite):
    def __init__(self, owner, angle):
        super().__init__(middle, motionful)
        self.image = BULLETS["player_bullet"]
        self.angle = angle
        self.owner = owner
        self.rect_f = list(self.image.get_rect())
        self.set_pos()
        self.rect = pygame.Rect(*self.rect_f)
        self.speed = 1000
        self.xspeed = None
        self.yspeed = None
        self.set_change_coord()
        self.collider = Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], trigger=True)
        self.tag = "bullet"

    def set_pos(self):
        self.rect_f[X], self.rect_f[Y] = self.owner.rect_f[X] + self.owner.rect_f[W] // 2, self.owner.rect_f[Y] + \
                                         self.owner.rect_f[H] // 2
        if self.angle % 180 == 0:
            self.rect_f[Y] -= self.rect_f[H] // 2
        else:
            self.rect_f[X] -= self.rect_f[W] // 2

    def move(self):
        self.rect_f[X] += self.xspeed * self.tick
        self.rect_f[Y] += self.yspeed * self.tick
        self.rect = pygame.Rect(*self.rect_f)
        self.collider.move(self.xspeed * self.tick, self.yspeed * self.tick)

    def set_tick(self, tick):
        self.tick = tick

    def set_change_coord(self):
        if self.angle % 360 == 0:
            self.xspeed = self.speed
            self.yspeed = 0
        elif self.angle % 360 == 90:
            self.xspeed = 0
            self.yspeed = -self.speed
        elif self.angle % 360 == 180:
            self.xspeed = -self.speed
            self.yspeed = 0
        elif self.angle % 360 == 270:
            self.xspeed = 0
            self.yspeed = self.speed
        else:
            self.xspeed = self.speed / sqrt(1 + abs(tan(self.angle * pi / 180)))
            self.yspeed = self.xspeed * abs(tan(self.angle * pi / 180))
            if 90 < self.angle % 360 < 270:
                self.xspeed = -self.xspeed
            if 0 < self.angle % 360 < 180:
                self.yspeed = -self.yspeed

    def unit_collided(self, unit):
        if unit.tag != "player" and unit.tag != "bullet":
            self.delete_from_all()

    def delete_from_all(self):
        self.kill()
        self.collider.kill()
