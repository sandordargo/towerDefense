import tower
import random
import monster

class Field:
    def __init__(self, towers):
        self.towers = towers
        self.monsters = []

    def add_new_monster(self):
        self.monsters.insert(0, monster.Monster())

    def get_tower_at_position(self, position):
        for t in self.towers:
            if t.position == position:
                return t
        return None

    def is_tower_at_position(self, position):
        for t in self.towers:
            if t.position == position:
                return True
        return False

    def is_monster_at_position(self, position):
        for m in self.monsters:
            if m.position == position:
                return True
        return False

    @staticmethod
    def generate_field():
        held_positions = []
        towers = []
        for i in range(5):
            pos = random.randint(0, 49)
            while pos in held_positions:
                pos = random.randint(0, 49)
            held_positions.append(pos)
            fp = random.randint(3, 8)
            lr = random.randint(0, 2)
            t = tower.Tower(pos, fp, lr)
            towers.append(t)

        field = Field(towers)
        return field
