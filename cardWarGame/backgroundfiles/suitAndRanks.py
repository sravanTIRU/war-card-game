"""
Module defining the suits, ranks, and values for a standard deck of playing cards.

Constants:
- suits (tuple): A tuple containing the four suits - ('Hearts', 'Diamonds', 'Spades', 'Clubs').
- ranks (tuple): A tuple containing the ranks of the cards from Two to Ace.
- values (dict): A dictionary mapping each rank to its numerical value in a standard deck.

Example Usage:
    from suitAndRanks import suits, ranks, values

    # Accessing the suits
    print(f"Suits: {suits}")

    # Accessing the ranks
    print(f"Ranks: {ranks}")

    # Accessing the values
    print(f"Values: {values}")
"""


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
