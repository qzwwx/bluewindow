import sys
import pygame
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet

screen = pygame.display.set_mode((800,600))


ship = Ship(screen)
bullets = Group()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(ship,screen)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            ship.moving_left = False
            ship.moving_right = False
            ship.moving_up = False
            ship.moving_down = False
    screen.fill((230,230,230))
    ship.blitme()
    ship.update()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    bullets.update()

    pygame.display.flip()
