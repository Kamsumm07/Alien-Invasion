import pygame



class Car:
    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()
        self.image = pygame.image.load('images/car_black_3.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.car_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.car_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

#main car but has the ability to shoot to protect the escort car

