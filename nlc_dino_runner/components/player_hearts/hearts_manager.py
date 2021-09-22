
from nlc_dino_runner.components.player_hearts.hearts import Heart
from nlc_dino_runner.utils.constants import HEART_COUNTER


class HeartsManager:
    def __init__(self):
        self.hearts_counter = HEART_COUNTER

    def draw(self, screen):
        x_position = 10
        for counter in range(self.hearts_counter):
            heart = Heart(x_position)
            x_position += 30
            heart.draw(screen)

    def reset_counter_hearts(self):
        self.hearts_counter = HEART_COUNTER
