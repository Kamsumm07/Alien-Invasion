import pygame
import sys
from pygame.sprite import Sprite


class Car:
    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()
        self.image = pygame.image.load('images/car_black_3.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
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

class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,255)
        self.car_speed = 1.5
        self.bullet_speed = 3.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 10
class Bullet(Sprite):
    def __init__(self, rg_game):
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = rg_game.car.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class RacingGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Racing Game")
        self.car = Car(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.car.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = False

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.car.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


#trying to figure out this part, keeping the car in edges while having a background, not working as of rn.
import pygame
background = [
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 2, 2, 1, 1, 0, 0, ],
]

TILE_SIZE = 205
road = pygame.image.load("images/road_sand87.png")
tile_rect = road.get_rect()
def draw_background(bg_size):
    bg = pygame.Surface(bg_size)
    for everything, grid_list in enumerate(background):
        for stuff, grid_element in enumerate(background_list):
            bg.blit(road[grid_element], (everything*TILE_SIZE, stuff*TILE_SIZE))
    return bg


if __name__ == '__main__':
    rg = RacingGame()
    rg.run_game()