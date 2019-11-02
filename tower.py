class Tower:
    def __init__(self, position, firePower, lengthOfRegeneration):
        self.position = position
        self.firePower = firePower
        self.lengthOfRegeneration = lengthOfRegeneration
        self.canFireInNTurns = lengthOfRegeneration

    def __repr__(self):
        return str(self.firePower)
