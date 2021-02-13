from fortune import Fortune
from teller import Teller
import time

# generate fortunes
fortunes = {}
for x in range(8):
    num = x+1
    if x % 2 == 0:
        fortuneText = 'crappy fortune'
    else:
        fortuneText = 'happy fortune'

    fortunes[num] = Fortune(num, f'{fortuneText} {num}!')

# generate teller
teller = Teller(["blue", "red", "green", "yellow"], False, fortunes)

def print_colors():
    print("the great paku-paku shows these colors. choose one:")
    print(teller.colors)

def print_numbers():
    print('the paku-paku shows these numbers:')
    for fortune in teller.fortunes:
        print(f'{fortune}...')
    print('choose wisely...')

# todo: the game
play = True
while play:
    print("what do you ask of the all powerful paku-paku?")
    question = input()
    
    print("ahhh yes, i see--you're curious indeed.")
    print_colors()
    color = input()

    while not teller.colors.__contains__(color):
        print("the paku-paku does not recognize your choice...")
        print_colors()
        color = input()
    
    print(f'an interesting choice...{color}')
    print(f'{color} has {len(color)} letters...')
    for x in range(len(color)):
        time.sleep(.5)
        teller.toggle()
        print(x+1)
    
    print_numbers()
    number = input()

    while not teller.fortunes.keys().__contains__(int(number)):
        print('the paku-paku insists on one of its displayed numbers...')
        print_numbers()
        number = input()

    print('ahhh your fortune is revealed:')
    print(f'{teller.fortunes[int(number)].fortune}')

    print('\nwould you care to ask another question?')
    playAgain = input()
    while playAgain != "yes" and playAgain != "no":
        print('the paku-paku desires a "yes" or "no"')
        playAgain = input()
    
    play = playAgain == "yes"