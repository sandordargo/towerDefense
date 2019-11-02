import field
import renderer
import random
import sys


class Game:
    def __init__(self):
        self.renderer = renderer.Renderer()
        self.field = field.Field.generate_field()

    def nextTurn(self):
        self.updateField()
        self.renderer.render(self.field)
        self.quitIfGameEnded()

    def updateField(self):
        for tower in self.field.towers:
            tower.decreaseNextFireTime()
            self.field.monsters = tower.fireIfMonsterInRange(self.field.monsters)
        self.field.monsters = [m for m in self.field.monsters if m.health_point > 0]
        for monster in self.field.monsters:
            monster.move_forward()
        if random.random() > 0.8:
            self.field.add_new_monster()

    def quitIfGameEnded(self):
        for m in self.field.monsters:
            if m.position >= 50:
                print("Monsters won")
                sys.exit()


if __name__ == "__main__":
    game = Game()
    for _ in range(100):
        game.nextTurn()
    print('Player won')
