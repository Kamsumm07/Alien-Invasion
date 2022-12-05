class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 255)
        self.car_speed = 6
        self.bullet_speed = 8
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10
        self.alien_speed = 7.5
        self.alien_frequency = 0.015
        self.car_limit = 2

#main settings class which controlls the screen height and length as well as the speeds of the enemies and players