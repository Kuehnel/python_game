from controllers.HelperController import load_image_scaled
from models.Enemy import Enemy


class Trap(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.attack_strength = 40

        self.width = 32
        self.height = 32

        self.img = load_image_scaled('sprites/traps', 'spikes.png', 2)