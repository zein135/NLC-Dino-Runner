import pygame.time

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstaclesManager():

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            # Rect1.colliderect(Rect2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                    continue
                game.playing = False
                pygame.time.delay(500)
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list.clear()
# Clase 4 - Colisiones