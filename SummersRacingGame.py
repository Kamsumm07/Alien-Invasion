import pygame
import sys
from random import random
from pygame import mixer
from Car import Car
from Car2 import Car2
from Settings import Settings
from Bullet import Bullet
from Motor import Motor
from GameStats import GameStats
from Background import Background

class RacingGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((910, 650))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Racing Game")
        self.car = Car(self)
        self.car2 = Car2(self)
        self.background = Background(self)
        self.bullets = pygame.sprite.Group()
        self.motors = pygame.sprite.Group()
        self.stats = GameStats(self)

    def run_game(self):
        self._background_music()

        while self.stats.game_active:
            self._check_events()
            if self.stats.game_active:
                self.car.update()
                self.car2.update()
                self._update_bullets()
                self._update_motors()
                self._create_motor()
            self._update_screen()

        Font = pygame.font.SysFont('Arial', 60)
        game_over_text = Font.render(f"GAME OVER", True, (200, 200, 200))
        self.screen.fill((0, 0, 0))
        self.screen.blit(game_over_text, (300, 400))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _background_music(self):
        pygame.mixer.music.load("music/Assets_Audio_music.ogg")
        pygame.mixer.music.play(-1)
#inputs background music

    def _car_hit(self):
        if self.stats.cars_left > 0:
            self.stats.cars_left -= 1
            self.motors.empty()
            self.bullets.empty()
            #self.car.center_car()
        else:
            self.stats.game_active = False
#when motorcycles hit car minus 1 life


    def _create_motor(self):
        if random() < self.settings.motor_frequency:
            motor = Motor(self)
            self.motors.add(motor)
            print(len(self.motors))
#creating the mot0rycle and how many come through

        Font = pygame.font.SysFont('Arial', 30)
        score_text = Font.render(f"SCORE: {len(self.motors)}", True, (0, 0, 0))
        self.screen.blit(score_text, (15, 20))
#shows the score of the game by how many motorcycles you pass

    def _update_motors(self):
        self.motors.update()
        if pygame.sprite.spritecollideany(self.car, self.motors):
            self._car_hit()
        if pygame.sprite.spritecollideany(self.car2, self.motors):
            self._car_hit()

#when the car and motorycles collide it signals it got hit
    def _check_bullet_motor_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.motors, True, True)
#same thing but just for bullet

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
#used for exiting the game

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = True
        elif event.key == pygame.K_d:
            self.car2.moving_right = True
        elif event.key == pygame.K_a:
            self.car2.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            bullet_sound = mixer.Sound("music/laser.wav")
            bullet_sound.play()
        elif event.key == pygame.K_q:
            sys.exit()

#events for main shooter car to move and also hear sound blasts
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        elif event.key == pygame.K_d:
            self.car2.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = False
        elif event.key == pygame.K_a:
            self.car2.moving_left = False
#events for cargo car to move left and right
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_motor_collisions()
#if bullet hits something then it collides if not then its removed essentially

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
#fires bullet

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.background.blitme()
        self.car.blitme()
        self.car2.blitme()
        self._create_motor()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.motors.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    rg = RacingGame()
    rg.run_game()

    
