#!/usr/bin/env python
# coding: utf-8

# In[1]:


#GAME SETUP

import random


# In[2]:


#SOME LISTS AND DICTIONARIES TO BE USED THROUGHOUT
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[3]:


#CARD CLASS
class Card:
    
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[4]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]     #this is an empty list
        for suit in suits:
            for rank in ranks:
                created_class=Card(rank,suit)
                self.all_cards.append(created_class)
                
    def shuffle_cards(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()   #removes the card from top of the deck


# In[5]:


#PLAYER CLASS
'''
The player must be able to:(i)HIT-add cards to his hand
                           (ii)STAND-stop adding cards
                           (iii)Total the sum of his/her cards
'''

class Player:
    
    def __init__(self,name):
        self.name=name
        self.player_cards=[]
        
    def take_hit(self,new_cards):
        if type(new_cards)==type([]):            #for adding multiple cards
            self.player_cards.extend(new_cards)
            
        else:
            self.player_cards.append(new_cards)    #for adding a single card
            
    def total_value(self):
        total_val=0
        for i in  range(len(self.player_cards)):
            total_val=total_val+self.player_cards[i].value
            
        return total_val
        


# In[6]:


class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,depamt):
        self.balance=self.balance+depamt

        
    def withdraw(self,drawamt):
       
            self.balance=self.balance-drawamt
           
            
       
    def __str__(self):
        return f"{self.owner}\nAccount balance:{self.balance}"
        
        


# In[7]:


def blackjack_check(player_class):
    if player_class.total_value()==21:
        
        print("BLACKJACK!!!")
        print("You win!")
        return 1
    else:
        return 0


# In[8]:


def bust_check(player_class):
    if player_class.total_value()>21:
        
        print("BUSTED!!!")
        print("You lose!")
        return 1
    else:
        return 0
    


# In[9]:


def score_check(player_class,dealer_class):
    player_total=player_class.total_value()
    dealer_total=dealer_class.total_value()
    
    global play_on
    play_on=False
    
    if player_total<dealer_total:
        print("You lose!!!")
        print("You lost the bet!")
         
        bank_withdraw(player_acc,bet_amt)
        bank_deposit(dealer_acc,bet_amt)
        print(f"Current balance:{player_acc.balance}")
        
        
        
    elif player_total>dealer_total:
        print("You win!!!")
        print("You won  the bet!")
                   
                    
        bank_withdraw(dealer_acc,bet_amt)
        bank_deposit(player_acc,bet_amt)
        print(f"Current balance:{player_acc.balance}")
                    
       
   
    elif dealer_total==21:
        print("Dealer got a BLACKJACK!!!")
        print("You lose!!")
        print("You lost the bet!")
                   
        bank_withdraw(player_acc,bet_amt)
        bank_deposit(dealer_acc,bet_amt)
        print(f"Current balance:{player_acc.balance}")
       
    elif dealer_total>21:
        print("Dealer BUSTED!!!")
        print("You win!!\n")
        print("You won  the bet!")
                   
        
        bank_withdraw(dealer_acc,bet_amt)
        bank_deposit(player_acc,bet_amt)
        print(f"Current balance:{player_acc.balance}")
                    
       
    else:
        print("GAME TIE!!!")
       


# In[10]:


def ask_hit(player_class,my_deck):
    print("Do you want to HIT or STAND?")
    resp=int(input("Enter 1 to HIT.\nEnter 2 to STAND.\n"))
    
    if resp==1:
        player_class.take_hit(my_deck.deal_one())
        print("After hit your cards are:")
        for card in player_class.player_cards:
            print(card)
            print(f'{card.value}')
        print(f'Value of your hand:{player_class.total_value()}')
    else:
        global hit
        hit=False
        global game_on
        game_on=False
        


# In[11]:


def ace_value():
    print("What do you want the ACE value to be?[1 or 11]")
    
    ace=int(input)
    


# In[12]:


def bank_withdraw(account_class,betamt):
    account_class.withdraw(betamt)


# In[13]:


def play_again():
    ctn=input("Do you want to play again?[y/n]")
    
    if ctn=='y'or ctn=='Y':
        return True
    else:
        return False
    
        


# In[14]:


def bank_deposit(account_class,betamt):
    account_class.deposit(betamt)


# In[16]:


start_game=True
while start_game:
    
    print("WELCOME TO BLACKJACK!")
    
    dealer_acc=Account('Dealer',4000)
    player_acc=Account('Player',4000)


    amt='wrong'
    while amt=='wrong': 
        bet_amt=int(input("Enter your bet amount:"))
        if bet_amt>4000:
            print("Bet amount exceeds your account balance!!!!.")
        else:
            amt='right'

    #creating and shuffling the deck        
    bj_deck=Deck()
    bj_deck.shuffle_cards()


    #creating player and dealer
    player=Player('Player')
    dealer=Player('Dealer')

    #dealing cards to the dealer and player
    dealer.take_hit([bj_deck.deal_one(),bj_deck.deal_one()])
    player.take_hit([bj_deck.deal_one(),bj_deck.deal_one()])

    #dealer's card
    print("DEALER'S CARD")
    print(dealer.player_cards[-1])
    print(f'{dealer.player_cards[-1].value}')

    #player's card
    print("YOUR CARDS")
    for card in player.player_cards:
        print(card)
        print(f'{card.value}')
    print(f'Value of your hand:{player.total_value()}')

        
    play_on=True
    while play_on:
    
    

        game_on=True

        while game_on:
            hit=True
            while hit:
                #check for blackjack
                bj=blackjack_check(player)
                if bj==1:
                    player_acc.deposit(2*bet_amt)
                    dealer_acc.withdraw(2*bet_amt)
                    print("You won double the bet!")
                    print(f"Current balance:{player_acc.balance}")
                    
                    game_on=False
                    hit=False
                    play_on=False
                    break
                else:
                    pass

                #check for bust
                bust=bust_check(player)
                if bust==1:
                    player_acc.withdraw(bet_amt)
                    dealer_acc.deposit(bet_amt)
                    print("You lost the bet!")
                    print(f"Current balance:{player_acc.balance}")
                    
                    game_on=False
                    hit=False
                    play_on=False
                    break
                else:
                    pass

                #ask for hit
                ask_hit(player,bj_deck)
    
         
       
        
        
    
        


        if bj==1 or bust==1:
            break

        player_total=player.total_value()
        print(f'Value of your hand:{player_total}')



        while dealer.total_value()<17:
            dealer.take_hit(bj_deck.deal_one())

        dealer_total=dealer.total_value()
        print(f'Value of dealer hand:{dealer_total}')

        score_check(player,dealer)
        
         

       
        
    #displaying the balance
    print("Balance:")
    print(player_acc)
    print(dealer_acc)



    start_game=play_again()
    if start_game==False:
        print("Thank you for playing!")














# # 

# In[ ]:





# In[ ]:





# In[ ]:




