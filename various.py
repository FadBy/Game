import pygame

collider_group = pygame.sprite.Group()

rooms = []
background = []
motionful = []
middle = []
object_sprites = []
interface_content = []
enemies = pygame.sprite.Group()
decors = []
arenas = []
transes = []
spawns = pygame.sprite.Group()
animations = []

size = width, height = 1280, 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, pygame.NOFRAME)

VERTICAL_SPRITE = 0
FULL_CORNER_SPRITE = 1
NOT_FULL_CORNER_SPRITE = 2
WALL_SPRITE = 3

X = 0
Y = 1
W = 2
H = 3

METR = 75
WIDTH_WALL_COLLIDER = 0.75
WIDTH_UNIT_COLLIDER = 0.2
HEIGHT_UNIT_COLLIDER = 0.5
INDENT_UNIT_COLLIDET = 0.2

FPS = 40

COUNT_OF_ILLUSIONS = 3

COUNT_OF_ENEMIES = 0
SPEED_BULLET_PLAYER = 800
SPEED_BULLET_ENEMY = 500
ANGLE_ZERO = 0.01

NOCLIP = False
GOD = False
DELETE_ENEMIES = False

SIZE_ROOM = [20, 16]
SIZE_TRANS = [14, 4]
SIZE_HUB = [14, 7]
SIZE_TRANSHUB = [4, 20]

COUNT_TYPES_ENEMIES = 2

GET_FIRST_WEAPON = 2

COUNT_OF_ARENAS = 4

koef_dif = 1.25
