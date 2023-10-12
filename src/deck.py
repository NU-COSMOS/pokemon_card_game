import json
from attrdict import AttrDict
from src.card import Card, Monster, Energy

class Deck:
    def __init__(self, deck_path: str) -> None:
        self.deck_path = deck_path
        self.deck = self.load_deck()

        for card in self.deck:
            print(card.name, card.type)

    def load_deck(self) -> list[Card]:
        with open(self.deck_path) as f:
            deck_dict = AttrDict(json.load(f))
        
        deck = []
        for card in deck_dict.cards:
            if card.type == "monster":
                deck.append(Monster(card))
            elif card.type == "energy":
                deck.append(Energy(card))

        return deck