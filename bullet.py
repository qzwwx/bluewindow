import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ship,screen):
        super().__init__()
        self.rect = pygame.Rect(0,0,3,15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.screen = screen
        self.color = (60,60,60)

    def update(self):
        self.rect.y -= 1

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
