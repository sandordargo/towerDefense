import field


class Renderer:
    def render(self, field_to_show):
        print("current state of field:")
        print(50 * "-")
        monster_line = ""
        for i in range(50):
            if field_to_show.is_monster_at_position(i):
                monster_line += "M"
            else:
                monster_line += "-"
        print(monster_line)

        tower_line = ""
        for i in range(50):
            if field_to_show.is_tower_at_position(i):
                tower_line += str(field_to_show.get_tower_at_position(i))
            else:
                tower_line += "-"
        print(tower_line)
