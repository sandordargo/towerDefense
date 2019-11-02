import monster

class Tower:
    def __init__(self, position, firePower, lengthOfRegeneration):
        self.position = position
        self.firePower = firePower
        self.lengthOfRegeneration = lengthOfRegeneration
        self.canFireInNTurns = lengthOfRegeneration

    def decreaseNextFireTime(self):
        self.canFireInNTurns -= 1

    def fireIfMonsterInRange(self, monsters):
        if not monsters:
            return []
        monsters.sort(key=lambda x: self.position - x.get_position())
        candidate = monsters[0]
        if abs(self.position - candidate.get_position()) <= self.firePower and self.canFireInNTurns == 0:
            candidate.health_point -= 1
            self.canFireInNTurns = self.lengthOfRegeneration
        return monsters

    def __repr__(self):
        return str(self.firePower)
