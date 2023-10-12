import json
from attrdict import AttrDict
from src.card import Monster, Energy


class Deck:
    def __init__(self, deck_path: str) -> None:
        self.deck_path = deck_path
        self.deck = self.load_deck()

    def load_deck(self) -> list[Monster | Energy]:
        """デッキの読み込み"""
        with open(self.deck_path) as f:
            deck_dict = AttrDict(json.load(f))
        
        # カードの読み込み
        deck = []
        for card in deck_dict.cards:
            if card.type == "monster":
                deck.append(Monster(card))
            elif card.type == "energy":
                deck.append(Energy(card))

        # デッキ所有者
        self.owner = deck_dict.owner

        return deck