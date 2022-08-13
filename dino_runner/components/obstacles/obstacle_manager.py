import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import  Birds
from dino_runner.utils.constants import SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.type = type

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            for obstacle in self.obstacles:
                obstacle.update(game.game_speed, self.obstacles)
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if not game.player.shield:
                        pygame.time.delay(500)
                        game.playing = False
                        break


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.playing = False
                    break
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 
