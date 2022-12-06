import pygame
from pygame.sprite import Sprite
from random import randint

class Motor(Sprite):
    def __init__(self, rg_game):
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.image = pygame.image.load('images/redmot.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen.get_rect().top
        motor_top_max = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, motor_top_max)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.motor_speed
        self.rect.y = self.y

#red motercycles which are used as the enemies. Go from top of screen to bottom and removed when hit the bottom.