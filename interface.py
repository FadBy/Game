from various import *
from sprites import *
from sprite import Sprite
from group import Group
import pygame
from math import ceil


class Interface(Group):
    def __init__(self, player):
        super().__init__()
        interface_content.append(self)
        self.player = player
        self.tag = "health"
        self.health = player.health
        self.healths = []
        self.ammo_numbers = []
        self.bandolier_numbers = []
        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0
        self.dividing_line = None

        self.coord_ammo = [width - 85, height - 130]
        self.coord_bandolier = [width - 85, height - 60]
        self.distance_symbols = 20
        self.coord_divide = [width - 90, height - 150]
        self.coord_weapon = [width - 250, height - 150]
        self.coord_health = [20, 30]
        self.distance_hp = 75
        self.weapon = self.player.weapon
        self.set_interface()

    def set_interface(self):
        self.dividing_line = Sprite(self)
        self.dividing_line.image = PLAYER["dividing_line"]
        self.dividing_line.rect_f = list(self.dividing_line.image.get_rect())
        self.dividing_line.rect_f[X], self.dividing_line.rect_f[Y] = self.coord_divide[X], self.coord_divide[Y]
        self.dividing_line.rect = pygame.Rect(self.dividing_line.rect_f)
        self.display_hp()
        self.display_ammo()
        self.display_bandolier()
        self.set_weapon()

    def set_weapon(self):
        self.weapon.kill()
        self.player.weapon.set_in_interface(self.coord_weapon[X], self.coord_weapon[Y])
        self.player.weapon.groups.append(self)
        self.add(self.player.weapon)
        self.weapon = self.player.weapon

    def display_hp(self):
        l = len(self.healths)
        for i in range(l):
            self.healths[0].kill()
        for i in range(ceil(self.health)):
            sprite = Sprite(self, self.healths)
            sprite.image = PLAYER["health_point"]
            sprite.rect_f = list(sprite.image.get_rect())
            sprite.rect_f[X], sprite.rect_f[Y] = self.coord_health[X] + i * self.distance_hp, self.coord_health[Y]
            sprite.rect = pygame.Rect(sprite.rect_f)

    def display_ammo(self):
        for i in range(len(self.ammo_numbers)):
            self.ammo_numbers[0].kill()
        for i in range(len(str(self.ammo_in_magazine))):
            filled = Sprite(self, self.ammo_numbers)
            filled.image = PLAYER[str(self.ammo_in_magazine)[i]]
            filled.rect_f = list(self.dividing_line.image.get_rect())
            filled.rect_f[X], filled.rect_f[Y] = self.coord_ammo[X] + i * self.distance_symbols, self.coord_ammo[Y]
            filled.rect = pygame.Rect(filled.rect_f)

    def display_bandolier(self):
        for i in range(len(self.bandolier_numbers)):
            self.bandolier_numbers[0].kill()
        for i in range(len(str(self.bandolier))):
            reserve = Sprite(self, self.bandolier_numbers)
            reserve.image = PLAYER[str(self.bandolier)[i]]
            reserve.rect_f = list(self.dividing_line.image.get_rect())
            reserve.rect_f[X] = self.coord_bandolier[X] + i * self.distance_symbols
            reserve.rect_f[Y] = self.coord_bandolier[Y]
            reserve.rect = pygame.Rect(reserve.rect_f)

    def change_hp(self):
        self.health = self.player.health
        self.display_hp()

    def set_ammo(self):
        self.ammo_in_magazine = self.player.weapon.ammo_in_magazine
        self.bandolier = self.player.weapon.bandolier
        self.full_ammo = self.player.weapon.full_ammo
        self.display_ammo()
        self.display_bandolier()
