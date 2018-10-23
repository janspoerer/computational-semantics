# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.

# Ignore "double" wars


import random

class Deck:
    SUITE = 'H D S C'.split() # Hearts, Diamonds, Spades, Clovers
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self.cards = []
        for suite_indiv in Deck.SUITE:
            for rank in Deck.RANKS:
                self.cards.append(suite_indiv + rank)
        self.cards = self.shuffle()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append(card)
        return ", ".join(cards)

    def split_in_half(self):
        mid = len(self.cards) // 2
        left = self.cards[:mid]
        right = self.cards[mid:]
        return [left, right]

    def shuffle(self):
        return random.sample(self.cards, len(self))

class Hand:
    def __init__(self, cards, player):
        self.cards = cards
        self.player = player

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        return card

    def remove_card(self, card_index):
        return self.cards.pop(card_index)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def still_has_cards(self):
        if len(self.hand) > 0:
            return true
        else:
            return false

    def turn_around_card(self):
        return self.hand.remove_card(0)

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
deck = Deck()
computer = Player("Computer", deck.split_in_half()[0])
player = Player("Player1", deck.split_in_half()[1])

active = True
while active:
    user_input = input("Please type y to continue playing: ")
    if (user_input == "y") or (user_input == "Y"):
        computer_card = computer.turn_around_card()
        player_card = player.turn_around_card()
        if computer_card < player_card:
            player.hand.extend([computer_card, player_card])
        elif computer_card < player_card: # If values are equal, cards are just put back
            player.hand.append(player_card)
            computer.hand.append(computer_card)
        else:
            computer.hand.extend([player_card, computer_card])
    else:
        break

if len(computer.hand) < len(player.hand):
    print("You won!")
elif len(computer.hand) == len(player.hand):
    print("Stalemate!")
else:
    print("The computer won!")
