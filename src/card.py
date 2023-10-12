class Card:
    def __init__(self, card) -> None:
        self.card = card
        self.name = self.card.name
        self.type = self.card.type


class Monster(Card):
    def __init__(self, card) -> None:
        super().__init__(card)
        self.before = self.card.before
        self.properties = self.card.properties


class Energy(Card):
    def __init__(self, card) -> None:
        super().__init__(card)
        self.property = self.card.property
        self.num = self.card.num