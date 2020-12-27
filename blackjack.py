list = [1,6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(list)
print('Lets play blackjack')
count = 0
while True:
    bet = input('Do you want to add a card? y/n\n')
    if bet == 'y':
        new = list.pop()
        print('You got a card of dignity %d' % new)
        count += new
    if count > 21:
        print('Sorry, but you lost')
        break
    elif count == 21:
        print('Congratulations, you won the blackjack!')
        break
    else:
        print('You have %d points.' %count)
    if bet == 'n':
        print('You have %d points and you have finished the game.' %count)
        break