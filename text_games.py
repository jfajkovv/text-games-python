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


class Player(object):
    '''Game participant.'''

    def __init__(self, name):
        self.name = name

####
###
### Card games
###
####

class Card(object):
    '''A standard game card.'''

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            re = f'[{self.rank}{self.suit}]'  # e.g. [Ah]
        else:
            re = '[Xx]'
        return re

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    '''Collection of cards. A representation of player's game cards
    -- to play with at hand.'''

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


class Deck(Hand):
    '''Extension of Hand. Source of game cards to play with
    -- a deck structure.'''

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

    def fill_in(self):
        for suit in SUITS:
            for rank in RANKS:
                self.stack_on(single_card=Card(rank=rank, suit=suit))

    def shuffle(self):

        from random import shuffle

        shuffle(self.card_set)

    def hand_out(self, hands, per_hand=1):
        if self.card_set:
            for rounds in range(per_hand):
                for hand in hands:
                    deck_top_card = self.card_set[0]
                    self.give(a_card=deck_top_card, other_hand=hand)
        else:
            print('game: deck depleted')


if __name__ == '__main__':
    print('info: text_games.py module')
    print('info: direct execution')
