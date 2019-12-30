from camera import Camera
from global_various import *
from wall import Wall


class Room(Camera):
    def __init__(self, image, x, y):
        super().__init__()
        self.add(surface_group)
        if image == "background_without_height.png":
            self.thickness = 30
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0], self.rect_f[1] = x, y
        self.rect = pygame.Rect(*self.rect_f)
        self.tag = "room"
        Wall(self, "hor_wall.png", 0, 0)
        Wall(self, "hor_wall.png", 0, 0 + self.rect_f[3] - self.thickness)
        Wall(self, "ver_wall.png", 0, 0)
        Wall(self, "ver_wall.png", 0 + self.rect_f[2] - self.thickness, 0)









