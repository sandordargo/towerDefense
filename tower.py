class Tower:
    def __init__(self, position, firePower, lengthOfRegeneration):
        self.position = position
        self.firePower = firePower
        self.lengthOfRegeneration = lengthOfRegeneration
        self.canFireInNTurns = lengthOfRegeneration

    def decreaseNextFireTime(self):
        self.canFireInNTurns -= 1

    def __repr__(self):
        return str(self.firePower)
