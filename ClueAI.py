import random

ALL_CLUE_CARDS = [
    "Colonel Mustard",
    "Professor Plum",
    "Mr Green",
    "Mrs Peacock",
    "Miss Scarlett",
    "Mrs White",
    "Airliner",
    "Automobile",
    "Train",
    "Hot Air Baloon",
    "Seaplane",
    "Limousine",
    "Coney Island",
    "Niagra Falls",
    "Miami Beach",
    "Lincoln Memorial",
    "Mt Rushmoore",
    "Old Faithful",
    "Golden Gate Bridge"
    "The Alamo"
    "Hoover Dam",
]
ALL_DETECTIVE_ACTION_CARDS = []


class OtherPlayer:
    def __init__(self):
        self.guesses
        self.disproves


class ClueAI:
    def __init__(self, num_players, my_clue_cards):
        self.my_clue_cards = my_clue_cards
        self.my_detective_action_cards
        other_players = []
        for i in range(num_players - 1):
            other_players.append(OtherPlayer())
        self.all_players = []


def deal_specific_card(cards, num1, num2):
    card = cards[random.randint(num1, num2)]
    cards.remove(card)
    return card


def deal_card(cards):
    return deal_specific_card(cards, 0, len(cards) - 1)


def play_clue(num_players):
    cards = ALL_CLUE_CARDS.copy()
    solution = [deal_specific_card(cards, 0, 5), deal_specific_card(cards, 5, 10), deal_specific_card(cards, 10, 18)]
