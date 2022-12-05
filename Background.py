import pygame



class Background:
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen

        self.image = pygame.image.load("images/roadbacl.png")

        self.screen_rect = self.screen.get_rect
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

#class used to set background as street