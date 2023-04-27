import random
from collections import Counter


class Card:
    RANKS = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack',
             12: 'Queen', 13: 'King'}
    SUITS = {1: 'Diamonds', 2: 'Clubs', 3: 'Hearts', 4: 'Spades'}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{Card.RANKS[self.rank]} of {Card.SUITS[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        for card in self.cards:
            self.score += self.get_card_score(card)

    def get_card_score(self, card):
        score = 0
        if card.rank == 1:
            score += 4
        elif card.rank == 11:
            score += 1
        elif card.rank == 12:
            score += 2
        elif card.rank == 13:
            score += 3

        suits = [c.suit for c in self.cards]
        if suits.count(card.suit) == 0:
            score += 5
        elif suits.count(card.suit) == 1:
            score += 2
        elif suits.count(card.suit) == 2:
            score += 1

        return score

    def __str__(self):
        sorted_cards = sorted(self.cards, key=lambda x: (x.suit, x.rank))
        cards_str = "\n".join([str(card) for card in sorted_cards])
        return f"Cards in hand:\n{cards_str}"


def deal_cards(deck):
    player1 = Hand()
    player2 = Hand()

    for i in range(13):
        card = deck.pop()
        player1.add_card(card)
        card = deck.pop()
        player2.add_card(card)

    return player1, player2


def rank_game_score(total_score):
    if total_score >= 35:
        return "Grand Slam"
    elif total_score >= 31:
        return "Small Slam"
    elif total_score >= 25:
        return "Game"
    elif total_score >= 19:
        return "Part Score"
    else:
        return "Pass"


def play_game():
    deck = Deck()
    deck.shuffle()

    player1_hand = Hand()
    player2_hand = Hand()

    # Deal 13 cards to each player
    for i in range(13):
        player1_hand.add_card(deck.pop())
        player2_hand.add_card(deck.pop())

    # Score each player's hand
    player1_hand.calculate_score()
    player2_hand.calculate_score()
    player1_score = player1_hand.score
    player2_score = player2_hand.score

    return player1_score + player2_score


def play_multiple_games(num_games):
    rank_counts = Counter()

    for i in range(num_games):
        # Create a new deck and shuffle it
        deck = Deck()
        deck.shuffle()

        # Deal the cards to two players
        player1_hand = Hand()
        player2_hand = Hand()
        for j in range(13):
            player1_hand.add_card(deck.pop())
            player2_hand.add_card(deck.pop())

        # Calculate the score of each hand
        player1_hand.calculate_score()
        player2_hand.calculate_score()

        # Rank the game score
        total_score = player1_hand.score + player2_hand.score
        rank = rank_game_score(total_score)

        # Update the rank counts
        rank_counts[rank] += 1

    # Print the probability distribution for each rank
    total_games = sum(rank_counts.values())
    for rank, count in rank_counts.items():
        probability = count / total_games
        print(rank + ":", probability)

