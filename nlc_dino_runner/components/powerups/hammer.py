
from nlc_dino_runner.components.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER_TYPE, HAMMER, SCREEN_WIDTH


class Hammer(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

class HammerThowed():

    def __init__(self):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.y = 310
        self.rect.x = 20

    def update_hammer(self, player, game_speed=21):
        print("Moviendo")
        self.rect.x += game_speed
        if self.rect.x > SCREEN_WIDTH:
            player.hammer = False
            player.throwing_hammer = False

    def draw_hammer(self, screen):
        screen.blit(self.image, self.rect)
