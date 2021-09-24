import pygame

from nlc_dino_runner.components import text_utils
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.components.player_hearts.hearts_manager import HeartsManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils.constants import TITTLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, LARGE_CACTUS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacles_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.hearts_manager = HeartsManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.high_score = 0

    def run(self):
        self.obstacles_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.hearts_manager.reset_counter_hearts()
        self.high_score = max(self.high_score, self.points)
        self.points = 0
        self.playing = True

        while self.playing:
            self.event()
            self.update()
            self.draw()
        # pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.screen)
        self.obstacles_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        if self.player.throwing_hammer:
            self.player.hammer_throwed.update_hammer(self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.hearts_manager.draw(self.screen)
        if self.player.throwing_hammer:
            self.player.hammer_throwed.draw_hammer(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)
        self.player.check_hammer(self.screen)


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        # La imagen se mueve
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execcute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        message = "Press any key to "
        if self.death_count == 0:
            message += "Start"
        else:
            message += "Restart"
        text, text_rect = text_utils.get_centered_message(message)
        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count), height=half_screen_height + 50)
        self.screen.blit(death_score, death_score_rect)

        previous_score, previous_score_rect = text_utils.get_centered_message("Your Score: " + str(self.points), height=half_screen_height + 90)
        self.screen.blit(previous_score, previous_score_rect)

        self.high_score = max(self.points, self.high_score)
        high_score, high_score_rect = text_utils.get_centered_message("High Score: " + str(self.high_score), height=half_screen_height + 130)
        self.screen.blit(high_score, high_score_rect)

        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, half_screen_height - 150))

# Clase 2: Ventana, Background

# Clase 5 - Creacion del score y menu