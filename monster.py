class Monster:
    def __init__(self):
        self.position = 0
        self.health_point = 10

    def __repr__(self):
        return "Monster(position={}, health_point={})".format(self.position, self.health_point)

    def move_forward(self):
        self.position += 1

    def get_position(self):
        return self.position
