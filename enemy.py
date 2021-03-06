from various import *
from character import Character
from functions import set_change_coord, calculate_angle
from sounds import *


class Enemy(Character):
    def __init__(self, player, x, y):
        super().__init__(middle, motionful, enemies)
        self.player = player
        self.tag = 'enemy'
        self.images = {}

        self.angle = 0
        self.side = "down"
        self.tick = 0
        self.change_y = 0
        self.change_x = 0

        self.weapon = None

        self.animation_frame = 4
        self.animation_duration = 0.3

        self.damage_collide = 0
        self.damage_bullet = 0

        self.speed = 0

    def move(self):
        if self.change_x == 0 and self.change_y == 0:
            coord = list(map(lambda x: x * self.tick, set_change_coord(self.angle, self.speed)))
        else:
            coord = [self.change_x, self.change_y]
            self.change_x = 0
            self.change_y = 0
        self.rect_f[X] += coord[X]
        self.rect_f[Y] += coord[Y]
        for i in self.colliders:
            self.colliders[i].move(coord[X], coord[Y])
        self.rotate()

    def attack(self):
        self.angle = calculate_angle(self.rect_f, self.player.rect_f)
        self.weapon.shoot(self.angle)
        self.rotate()

    def move_by_collider(self, x, y):
        if x != 0:
            self.change_x = x
        if y != 0:
            self.change_y = y

    def unit_collided(self, collider, unit):
        pass

    def kill(self):
        super().kill()
        for i in self.colliders:
            robo_dying.play()
            self.colliders[i].kill()

    def rotate(self):
        if 315 <= self.angle % 360 <= 360 or 0 <= self.angle <= 45:
            if self.side != "right":
                self.image = self.images["right"]
                self.side = "right"
        elif 45 <= self.angle % 360 <= 135:
            if self.side != "up":
                self.image = self.images["up"]
                self.side = "up"
        elif 135 <= self.angle % 360 <= 225:
            if self.side != "left":
                self.image = self.images["left"]
                self.side = "left"
        else:
            if self.side != "down":
                self.image = self.images["down"]
                self.side = "down"

