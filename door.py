from camera import Camera
from global_various import *
from collider import Collider


class Door(Camera):
    def __init__(self, wall, image, x, y):
        super().__init__()
        self.room = wall.room
        self.wall = wall
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0], self.rect_f[1] = x, y
        self.rect = pygame.Rect(*self.rect_f)
        self.collider = Collider(self, 0, 0, self.rect_f[2], self.rect_f[3])


