import random
from dino_runner.components.obstacles.sky import Sky

class Clouds(Sky):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 50
 