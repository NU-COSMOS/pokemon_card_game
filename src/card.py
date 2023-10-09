class Card:
    def __init__(self, name) -> None:
        self.name = name


class Monster(Card):
    def __init__(self, name) -> None:
        super().__init__(name)