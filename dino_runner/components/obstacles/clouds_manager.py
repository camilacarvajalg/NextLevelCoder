import pygame
from dino_runner.components.obstacles.clouds import Clouds
from dino_runner.utils.constants import CLOUD

class CloudsManager():
    def __init__(self):
        self.clouds = []
    def update(self, game):
        if len(self.clouds) == 0:
            self.clouds.append(Clouds(CLOUD))

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

