from fortune import Fortune
from teller import Teller

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
print(teller)
for x in teller.fortunes:
    print(fortunes[x])

# todo: the game
