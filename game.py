import field
import renderer


class Game:
    def __init__(self):
        self.renderer = renderer.Renderer()
        self.field = field.Field()

    def nextTurn(self):
        self.updateField()
        self.renderer.render(self.field)

    def updateField(self):
        pass


if __name__ == "__main__":
    game = Game()
    for _ in range(2):
        game.nextTurn()

