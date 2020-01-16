from player import Player
from room import Room
import time
from all_various import *
from test import *


def draw_all_sprites():
    for i in background:
        i.draw(screen)
    middle.sort(key=lambda x: x.rect[1] + x.rect[3])
    for i in middle:
        i.draw(screen)
    if TEST_COLLIDER:
        for i in motionless_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f), 5)
        for i in motionful_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f))


pygame.init()
player = Player()
sur1 = Room(TEXTURES_DEFAULT, width // 2 - 300, height // 2 - 300, 20, 10, [["left", 5], ["down", 2]])
sort_groups()
screen = pygame.display.set_mode(size, pygame.NOFRAME)

TEST_COLLIDER = False
PRINT_FPS = True

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.set_tick(clock.tick() / 1000)
    player.change_all_pos()
    player.check_colliders()
    player.change_all_pos()
    player.change_x = 0
    player.change_y = 0
    draw_all_sprites()
    pygame.display.flip()
    if player.check_pressed() == 'paused':
        paused = True
        little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
        while paused:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 350:
                            if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 290:
                                paused = False
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_continue'],
                                                                     (width // 2, width // 2))
                        if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 275:
                            if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 215:
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_options'],
                                                                     (width // 2, width // 2))
                        if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 199:
                            if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 137:
                                running = False
                                paused = False
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_exit'],
                                                                     (width // 2, width // 2))
                if event.type == pygame.MOUSEBUTTONUP:
                    little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
            screen.blit(little_menu, little_menu.get_rect(bottomright=(width * 3 // 4, height * 15 // 16)))
            pygame.display.flip()
    if PRINT_FPS:
        (print(int(clock.get_fps())))

pygame.quit()