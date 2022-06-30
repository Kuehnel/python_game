from models.Character import Character


class Enemy(Character):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

        self.attack_strength = 10

        self.attack_clock = 1

