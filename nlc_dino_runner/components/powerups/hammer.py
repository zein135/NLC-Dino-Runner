
from nlc_dino_runner.components.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER_TYPE, HAMMER, SCREEN_WIDTH, DEFAULT_TYPE


class Hammer(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

class HammerThowed():

    def __init__(self, pos_y):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.y = pos_y
        self.rect.x = 80

    def update_hammer(self, player):
        self.rect.x += 10
        if self.rect.x > SCREEN_WIDTH:
            player.throwing_hammer = False
            player.hammers_remain -= 1
            if player.hammers_remain == 0:
                player.type = DEFAULT_TYPE
                player.hammer = False

    def draw_hammer(self, screen):
        screen.blit(self.image, self.rect)
