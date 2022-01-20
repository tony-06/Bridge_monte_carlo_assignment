import sys

import pydealer

import copy

from collections import Counter


# pass a hand of cards and return the score
def get_score(hand):
    score = 0
    # count the number of each suits and add points based on the total
    for suit in pydealer.const.SUITS:
        suit_counter = 0
        for card in hand:
            if card.suit == suit:
                suit_counter += 1
        if suit_counter == 0:
            score += 5
            # print("5 points for having zero " + j)
        elif suit_counter == 1:
            score += 2
            # print("2 points for having one " + j)
        elif suit_counter == 2:
            score += 1
            # print("1 point for having two " + j)
        else:
            continue
    # count the face cards and add their points into the score
    for d in hand:
        if d.value == "Ace":
            score += 4
        # print("4 points for the " + str(d))
        elif d.value == "Jack":
            score += 1
            # print("1 points for the " + str(d))
        elif d.value == "Queen":
            score += 2
            # print("2 points for the " + str(d))
        elif d.value == "King":
            score += 3
            # print("3 points for the " + str(d))
        else:
            continue
    # print("\n" + str(score) + " points total\n")
    return score


# takes a counter with all scores/frequencies and sorts them into a new counter with the point scale and frequency
def sort_scores(raw_score_counter):
    points = Counter({"grand slam": 0, "small slam": 0, "game": 0, "part score": 0, "pass": 0})
    for a, b in raw_score_counter.items():
        if a > 35:
            points.update({"grand slam": b})
        elif a > 31:
            points.update({"small Slam": b})
        elif a > 25:
            points.update({"game": b})
        elif a > 19:
            points.update({"part score": b})
        else:
            points.update({"pass": b})
    return points


# pass the remaining deck and the number of simulations that you want to run as well as the players static score
def partner_score(dealer_stack, n, p_score):
    score_list = []
    for i in range(n):
        # not 100% percent sure this is needed but I was worried the function would modify the original stack
        temp_deck = copy.deepcopy(dealer_stack)
        # print line to verify that they length of the remaining deck is 39
        # print(len(temp_deck))
        # shuffle the temp deck
        temp_deck.shuffle()
        # deal 13 cards to the partner
        partner_deck = temp_deck.deal(13)
        # print line to verify partner deck was outputting correct hands and scores
        # print(partner_deck)
        # total the score for each iteration and add the static player score
        hand_score = get_score(partner_deck) + p_score
        # add the score from each iteration to a list
        score_list.append(hand_score)
    # return a counter container with the simulated scored and the number of times they occurred
    return sort_scores(Counter(score_list))


def new_game():
    while True:
        # creates a 52 card deck from pydealer
        new_deck = pydealer.Deck()
        # rank dictionary for easy reading output
        new_ranks = {"suits": {"Spades": 4, "Hearts": 3, "Clubs": 2, "Diamonds": 1}}
        # shuffle the deck
        new_deck.shuffle()
        # deal 13 cards to yourself
        player_hand = new_deck.deal(13)
        player_hand.sort(ranks=new_ranks)
        # calculate your score
        print("This is your hand :")
        print(player_hand)
        player_score = get_score(player_hand)
        print("\n Your hand is worth {} points".format(player_score))
        # number of simulations to run
        monte_carlo = 1000
        # get a container of all the scaled scores and their frequency
        partner_simulation = partner_score(new_deck, monte_carlo, player_score)
        print("\n After 1000 simulations, here is the estimated probability of each outcome:")
        for value, count in partner_simulation.items():
            chance = count / monte_carlo
            print('{} {:.2%}'.format(value, chance))
        while True:
            r = input("Press 1 to run another simulation or 0 to exit")
            if r == "1":
                break
            elif r == "0":
                sys.exit()
            else:
                print("Bad input")
