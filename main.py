from all_various import *
from player import *
from room import *


def sort_groups():
    rooms.sort(key=lambda x: x.rect_f[0], reverse=True)


def check_colliders():
    for i in motionful:
        colliders = pygame.sprite.spritecollide(i.collider, collider_group, False)
        if colliders:
            for j in colliders:
                if j.owner != i:
                    if j.trigger:
                        j.owner.unit_collided(i)
                    else:
                        j.default_collide(i)
                    if i.collider.trigger:
                        i.unit_collided(j.owner)


def change_all_pos():
    for i in rooms:
        i.move_camera(player.change_x, player.change_y)
    for i in collider_group:
        if i.owner.tag != "player":
            i.move_camera(player.change_x, player.change_y)
    for i in object_sprites:
        i.move_camera(player.change_x, player.change_y)
    for i in motionful:
        if i != player:
            i.move_camera(player.change_x, player.change_y)
            i.move()


def draw_all_sprites():
    for i in background:
        i.draw(screen)
    middle.sort(key=lambda x: x.rect[Y] + x.rect[H])
    for i in middle:
        i.draw(screen)
    if TEST_COLLIDER:
        for i in collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f), 5)


pygame.init()

player = Player()
sur1 = Room(TEXTURES_DEFAULT, width // 2 - 300, height // 2 - 300, 20, 10, [["left", 5], ["down", 2]])

sort_groups()

TEST_COLLIDER = False
PRINT_FPS = True

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninsg = False
    tick = clock.tick() / 1000
    for i in motionful:
        i.set_tick(tick)
    if player.check_pressed() == 'paused':
        paused = True
        while paused:
            little_menu = pygame.transform.scale(MENU['ingame_menu'], (width // 2, width // 2))
            screen.blit(little_menu, little_menu.get_rect(bottomright=(width * 3 // 4, height * 15 // 16)))
            pygame.display.flip()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 350:
                            if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 290:
                                paused = False
                        if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 199:
                            if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 137:
                                running = False
                                paused = False
    for i in motionful:
        i.set_tick(tick)
    change_all_pos()
    check_colliders()
    change_all_pos()
    player.change_x = 0
    player.change_y = 0
    draw_all_sprites()
    pygame.display.flip()
    if PRINT_FPS:
        (print(int(clock.get_fps())))

pygame.quit()
