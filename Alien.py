import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.image = pygame.image.load('images/redmot.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen.get_rect().top
        alien_top_max = self.settings.screen_width - self.rect.width
        self.rect.left = randint(0, alien_top_max)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_speed
        self.rect.y = self.y

#red motercycles which are used as the enemies. Go from top of screen to bottom and removed when hit the bottom.