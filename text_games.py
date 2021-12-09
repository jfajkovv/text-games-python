####
###
### General utilities
###
####

def ask_int_in_range(user_query, range_bottom, range_top):
    '''Returns an integer (as an answer to a question).'''

    reply = None
    while reply not in range(range_bottom, range_top + 1):
        reply = int(input('\t' + user_query))
    return reply


def ask_yes_no(user_query):
    '''Returns a "y" or "n" (as an answer to a question).'''

    reply = None
    while reply not in ('y', 'n'):
        reply = input('\t' + user_query).lower()
    return reply

####
###
### Card games
###
####

class Card(object):
    '''A standard game card.'''

    SUITS = (
        'c',  # clubs
        'd',  # diamonds
        'h',  # hearts
        's',  # spades
    )

    RANKS = (
        'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'J', 'Q', 'K'
    )

    def __init__(self, rank, suit, obverse_up=True):
        self.rank = rank
        self.suit = suit
        self.is_obverse_up = obverse_up

    def __str__(self):
        if self.is_obverse_up:
            re = f'[{self.rank}{self.suit}]'  # e.g. [Ah]
        else:
            re = '[Xx]'
        return re

    def flip(self):
        self.is_obverse_up = not self.is_obverse_up


class Hand(object):
    '''Collection of cards. A representation of player's game cards
    - to play with at hand.'''

    def __init__(self):
        self.card_set = []

    def __str__(self):
        if self.card_set:
            re = ''
            for card in self.card_set:
                re += str(card) + '\t'
        else:
            re = '<empty hand>'
        return re

    def stack_on(self, single_card):
        self.card_set.append(single_card)

    def give(self, a_card, other_hand):
        self.card_set.remove(a_card)
        other_hand.stack_on(single_card=a_card)

    def transfer_all(self, route):
        for card in self.card_set:
            self.give(a_card=card, other_hand=route)

    def clear(self):
        self.card_set = []
