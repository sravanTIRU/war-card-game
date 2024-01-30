"""
War Card Game:

Rules:
- The game is played with a standard deck of 52 cards.
- The deck is divided equally between two players.
- In each round, both players reveal the top card of their deck.
- The player with the higher-ranked card wins the round and takes both cards, placing them at the bottom of their deck.
- If there is a tie, a war is declared:
    - Each player places ten(10) cards face down, followed by one card face up.
    - The player with the higher-ranked face-up card wins all the cards on the table.
    - If there is another tie, the process repeats.
- The game continues until one player runs out of cards, and the other player is declared the winner.
- If the game reaches a maximum number of rounds (e.g., 5000 rounds), it ends in a tie.

Note:
- The ranks, suits, and values used in the game are based on standard playing card conventions.
"""


from backgroundfiles.deck import Deck
from backgroundfiles.player import Player


def check_for_winner(p1: Player, p2: Player) -> bool:
    """
    Checks if either player has run out of cards.

    Args:
        p1 (Player): The first player.
        p2 (Player): The second player.

    Returns:
        bool: True if either player has no cards left, False otherwise.
    """
    return len(p1.player_deck) < 1 or len(p2.player_deck) < 1


def deal_cards(p1: Player, p2: Player, new_deck: Deck):
    """
    Deals cards from the new deck to both players.

    Args:
        p1 (Player): The first player.
        p2 (Player): The second player.
        new_deck (Deck): The deck of cards to be used in the game.
    """
    p1.player_deck.extend(new_deck.pop_a_card() for _ in range(26))
    p2.player_deck.extend(new_deck.pop_a_card() for _ in range(26))


def print_win_condition(p1: Player, p2: Player):
    """
    Prints the winner of the game.

    Args:
        p1 (Player): The first player.
        p2 (Player): The second player.
    """
    print(f'\n{p1.name if len(p1.player_deck) < 1 else p2.name} won the game.'.upper())


def check_for_war_winner(p1: Player, p2: Player) -> bool:
    """
    Checks if either player has enough cards for a war.

    Args:
        p1 (Player): The first player.
        p2 (Player): The second player.

    Returns:
        bool: True if either player does not have enough cards for a war, False otherwise.
    """
    return len(p1.player_deck) < 10 or len(p2.player_deck) < 10


if __name__ == '__main__':
    # PLAYERS
    player_one = Player('harry')
    player_two = Player('manny')

    # creating new deck
    fresh_deck = Deck()

    # shuffling the deck
    fresh_deck.shuffle_deck()

    # dealing equal amount of cards for both players
    deal_cards(player_one, player_two, fresh_deck)

    # current round counter.
    current_round = 1
    max_rounds = 500
    wars_count = 0

    while True:
        if current_round > max_rounds:
            print(f"The game ends in a tie after {max_rounds} rounds. It's a tie.".upper())
            break
        print(f"Round {current_round}:".upper())

        # checking for winner
        if check_for_winner(player_one, player_two):
            print_win_condition(player_one, player_two)
            break

        # players placing one card on the board
        player_one_pool = []
        player_two_pool = []
        player_one_pool.append(player_one.pop_player_card())
        player_two_pool.append(player_two.pop_player_card())

        p1_top = player_one_pool[-1].value
        p2_top = player_two_pool[-1].value

        if p1_top > p2_top:
            player_one.player_deck.extend(player_one_pool)
            player_one.player_deck.extend(player_two_pool)
        elif p1_top < p2_top:
            player_two.player_deck.extend(player_one_pool)
            player_two.player_deck.extend(player_two_pool)
        else:
            print('\nWAR IS ON THE TABLE!!!')
            # Display cards of both players in the war
            print(f'{player_one.name}\'s cards: {", ".join(str(card) for card in player_one_pool)}')
            print(f'{player_two.name}\'s cards: {", ".join(str(card) for card in player_two_pool)}\n')
            wars_count += 1
            # Check if players have enough cards for a war
            if not check_for_war_winner(player_one, player_two):
                for i in range(10):
                    player_one_pool.append(player_one.pop_player_card())
                    player_two_pool.append(player_two.pop_player_card())
            else:
                # Handle the case when one of the players doesn't have enough cards for a war
                print_win_condition(player_one, player_two)
                break

        current_round += 1
    print(f"Number of wars happened: {wars_count}".upper())
