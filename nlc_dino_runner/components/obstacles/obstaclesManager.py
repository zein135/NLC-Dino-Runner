import pygame.time
import pygame
import random

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from nlc_dino_runner.components.obstacles.bird import Bird


class ObstaclesManager():

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(random.choice([Cactus(SMALL_CACTUS, 320), Cactus(LARGE_CACTUS, 300), Bird()]))
        for obstacle in self.obstacles_list:
            if type(obstacle) == Bird:
                obstacle.update_bird(game.player.step_index)
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.throwing_hammer:
                if game.player.hammer_throwed.rect.colliderect(obstacle.rect):
                    self.obstacles_list.remove(obstacle)
                    continue

            # Rect1.colliderect(Rect2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    game.hearts_manager.hearts_counter -= 1
                    if game.hearts_manager.hearts_counter > 0:
                        self.obstacles_list.remove(obstacle)
                    else:
                        game.playing = False
                        pygame.time.delay(500)
                        game.death_count += 1
                        game.game_speed = 20
                        break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list.clear()
# Clase 4 - Colisiones

