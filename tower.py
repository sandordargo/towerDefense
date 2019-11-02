import monster

class Tower:
    def __init__(self, position, firePower, lengthOfRegeneration):
        self.position = position
        self.firePower = firePower
        self.lengthOfRegeneration = lengthOfRegeneration
        self.canFireInNTurns = lengthOfRegeneration

    def __repr__(self):
        return "Tower(position={}, fire_power={}, " \
               "lengthOfRegeneration{}, canFireInNTurns={})".format(
            self.position, self.firePower, self.lengthOfRegeneration, self.canFireInNTurns
        )

    def decreaseNextFireTime(self):
        if self.canFireInNTurns > 1:
            self.canFireInNTurns -= 1

    def fireIfMonsterInRange(self, monsters):
        if not monsters:
            return []
        monsters.sort(key=lambda x: self.position - x.get_position())
        candidate = monsters[0]
        if abs(self.position - candidate.get_position()) <= self.firePower and self.canFireInNTurns == 0:
            candidate.health_point -= 1
            if candidate.health_point < 1:
                print('monster died')
            self.canFireInNTurns = self.lengthOfRegeneration
        return monsters

    def __str__(self):
        return str(self.firePower)
