class Monster:
    def __init__(self):
        self.position = 0
        self.health_point = 10

    def move_forward(self):
        self.position += 1
