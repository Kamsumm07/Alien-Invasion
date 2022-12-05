class GameStats:
    def __init__(self, rg_game):
        self.settings = rg_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.cars_left = self.settings.car_limit

#stats that count number of lives left