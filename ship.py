import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.centerx < 800:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.centerx >0:
            self.rect.centerx -= 1
        elif self.moving_up and self.rect.centery > 0 :
            self.rect.centery -= 1
        elif self.moving_down and self.rect.centery < 600 :
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image,self.rect)
