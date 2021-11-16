
from time import *
# BLACK JACK - CASINO
# PYTHON CODE BASE

# master
import  random
deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
random.shuffle(deck)

print(f'{"*"*58}\n Welcome to the game Casino - BLACK JACK !')
sleep(2)
print('So Finally You Are Here To Accept Your Fate')
sleep(2)
print('I Mean Your Fortune')
sleep(2)
print('Lets Check How Lucky You Are Wish You All The Best')
sleep(2)
print('Loading---')
sleep(2)

print('Still Loading---')
sleep(2)
print('So You Are Still Here Not Gone I Gave You Chance But No Problem May Be You Trust Your Fortune A Lot \n Lets Begin Then')
sleep(2)

d_cards = []    # Initialising dealer's cards
p_cards = []    # Initialising player's cards

while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print('The cards dealer has are X ',d_cards[1])

# Displaying the Player's cards
while len(p_cards) !=2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print("The total of player is ",sum(p_cards))
        print("The cards Player has are ",p_cards)
