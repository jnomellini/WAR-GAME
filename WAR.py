#!/usr/bin/env python
# coding: utf-8

# CARD
# SUIT, RANK, VALUE
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

three_of_clubs = Card("Clubs",'Three')

three_of_clubs.suit

three_of_clubs
two_hearts = Card("Hearts","Two")

print(two_hearts)

two_hearts.suit

two_hearts.rank

two_hearts.value

two_hearts.value == three_of_clubs.value

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()

new_deck.shuffle()

mycard = new_deck.deal_one()

print(mycard)

len(new_deck.all_cards)

bottom_card = new_deck.all_cards[-1]

print(bottom_card)

new_deck.shuffle()

print(new_deck.all_cards[0])

class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

new_player = Player("Jose")

print(new_player)

new_player.add_cards(mycard)

print(new_player)

print(new_player.all_cards[0])

new_player.add_cards([mycard,mycard,mycard])

print(new_player)

new_player.remove_one()

print(new_player)
