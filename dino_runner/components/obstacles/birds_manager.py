import pygame
from dino_runner.components.obstacles.bird import Birds
from dino_runner.utils.constants import BIRD

class BirdsManager():
    def __init__(self):
       self.birds = []

    def update(self, game):
        if len(self.birds) == 0:
           self.birds.append(Birds(BIRD))
           for bird in self.birds:
                bird.update(game.game_speed, self.birds)
                if game.player.dino_rect.colliderect(bird.rect):
                    if not game.player.shield:
                        pygame.time.delay(500)
                        game.playing = False
                        break


        for bird in self.birds:
            bird.update(game.game_speed, self.birds)
            if game.player.dino_rect.colliderect(bird.rect):
                if not game.player.shield:
                    game.playing = False
                    break
        
    def draw(self, screen):
        for bird in self.birds:
            bird.draw(screen) 

