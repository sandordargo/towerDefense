import field
import renderer


class Game:
    def __init__(self):
        self.renderer = renderer.Renderer()
        self.field = field.Field.generate_field()

    def nextTurn(self):
        self.updateField()
        self.renderer.render(self.field)

    def updateField(self):
        for tower in self.field.towers:
            tower.decreaseNextFireTime()
        for monster in self.field.monsters:
            monster.move_forward()


if __name__ == "__main__":
    game = Game()
    for _ in range(2):
        game.nextTurn()

