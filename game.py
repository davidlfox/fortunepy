from teller import Teller
import time
from eightball import EightBall

# generate teller
teller = Teller(["blue", "red", "green", "yellow"], range(8))

def print_colors():
    print("the great paku-paku shows these colors. choose one:")
    print(teller.colors)

def print_numbers():
    print('the paku-paku shows these numbers:')
    for fortune in teller.fortunes:
        print(f'{fortune+1}...')
    print('choose wisely...')

# the game
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
        print(x+1)
    
    print_numbers()
    number = input()

    while not teller.fortunes.__contains__(int(number)):
        print('the paku-paku insists on one of its displayed numbers...')
        print_numbers()
        number = input()

    print('ahhh your fortune is revealed:')
    # todo: should this be done earlier?
    eightBall = EightBall(question)
    response = eightBall.getFortune()
    print(response)

    print('\nwould you care to ask another question?')
    playAgain = input()
    while playAgain != "yes" and playAgain != "no":
        print('the paku-paku desires a "yes" or "no"')
        playAgain = input()
    
    play = playAgain == "yes"