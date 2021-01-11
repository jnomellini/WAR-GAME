#!/usr/bin/env python
# coding: utf-8

# In[105]:


# CARD
# SUIT, RANK, VALUE
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


# In[106]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[107]:


three_of_clubs = Card("Clubs",'Three')


# In[108]:


three_of_clubs.suit


# In[109]:


three_of_clubs.value


# In[110]:


two_hearts = Card("Hearts","Two")


# In[111]:


print(two_hearts)


# In[112]:


two_hearts.suit


# In[113]:


two_hearts.rank


# In[114]:


two_hearts.value


# In[115]:


two_hearts.value == three_of_clubs.value


# In[130]:


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


# In[132]:


new_deck = Deck()


# In[133]:


new_deck.shuffle()


# In[134]:


mycard = new_deck.deal_one()


# In[135]:


print(mycard)


# In[136]:


len(new_deck.all_cards)


# In[118]:


bottom_card = new_deck.all_cards[-1]


# In[119]:


print(bottom_card)


# In[120]:


new_deck.shuffle()


# In[126]:


print(new_deck.all_cards[0])


# In[150]:


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


# In[151]:


new_player = Player("Jose")


# In[152]:


print(new_player)


# In[156]:


new_player.add_cards(mycard)


# In[157]:


print(new_player)


# In[160]:


print(new_player.all_cards[0])


# In[161]:


new_player.add_cards([mycard,mycard,mycard])


# In[162]:


print(new_player)


# In[163]:


new_player.remove_one()


# In[164]:


print(new_player)


# In[ ]:





# In[ ]:




