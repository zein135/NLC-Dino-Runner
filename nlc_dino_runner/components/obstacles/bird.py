from nlc_dino_runner.components.obstacles.obstacles import Obstacles
from nlc_dino_runner.utils.constants import BIRD


class Bird(Obstacles):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = 250

    def update_bird(self, step_index):
        self.obstacle_type = step_index // 5
