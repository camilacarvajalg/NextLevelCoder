from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Hammer, self).__init__(self.image, self.type)
