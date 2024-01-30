"""Module for defining a Player class representing participants in a card game."""


class Player:
    """
    Represents a player in a card game.

    Args:
        name (str): The name of the player.

    Attributes:
        name (str): The name of the player.
        player_deck (list): A list containing `Cards` objects representing the player's hand.

    Methods:
        pop_player_card(): Removes the top card from the player's hand.
        collect_cards(cards_won): Adds one or more `Cards` objects to the player's hand.
        __str__(): Returns a formatted string representing the player and the number of cards in their hand.
    """
    def __init__(self, name):
        self.name = name.upper()
        self.player_deck = []

    def pop_player_card(self):
        """Removes the top card from the player's hand."""
        return self.player_deck.pop(0)

    def collect_cards(self, cards_won):
        """
        Adds one or more `Cards` objects to the player's hand.

        Args:
            cards_won (list or Cards): Either a list of `Cards` objects or a single `Cards` object.

        Returns:
            None
        """
        if isinstance(cards_won, list):
            self.player_deck.extend(cards_won)
        else:
            self.player_deck.append(cards_won)

    def __str__(self):
        """
        Returns a formatted string representing the player and the number of cards in their hand.

        Returns:
            str: A formatted string indicating the player's name and the number of cards in their hand.
        """
        return f'{self.name} has {len(self.player_deck)} cards in hand.'.upper()
