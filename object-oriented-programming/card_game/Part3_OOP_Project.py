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
        return [self.cards[:mid], self.cards[mid:]]

    def shuffle(self):
        return random.sample(self.cards, len(self))

class Hand:
    def __init__(self, cards):
        self.cards = cards

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
computer = Player("Computer", Hand(deck.split_in_half()[0]))
player = Player("Player", Hand(deck.split_in_half()[1]))

active = True
while (len(computer.hand) > 0) and (len(player.hand) > 0):
    user_input = input("Please type y to continue playing: ")

    if (user_input == "y") or (user_input == "Y"):
        computer_card = computer.turn_around_card()
        player_card = player.turn_around_card()

        computer_rank = Deck.RANKS.index(computer_card[1:])
        player_rank = Deck.RANKS.index(player_card[1:])

        if computer_rank < player_rank:
            player.hand.cards.extend([computer_card, player_card])
            print(player.name, " got a card! Player: ", str(len(player.hand)), ", Computer: ", str(len(computer.hand)))
        elif player_rank == player_rank: # If values are equal, cards are just put back
            player.hand.cards.append(player_card)
            computer.hand.cards.append(computer_card)
            print("Tie!")
        else:
            computer.hand.cards.extend([player_card, computer_card])
            print(computer.name, " got a card! Player: ", str(len(player.hand)), ", Computer: ", str(len(computer.hand)))
    else:
        break

if len(computer.hand) < len(player.hand):
    print("You won!")
elif len(computer.hand) == len(player.hand):
    print("Stalemate!")
else:
    print("The computer won!")
