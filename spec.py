# https://en.wikipedia.org/wiki/Paper_fortune_teller

# ----------
# data model
# ----------

    # FortuneTeller
    # ----------
    # has four colors
    # has eight numbers
    # has eight fortunes (one per number)
    # colors always "visible" (first choice)
    # only half of numbers are (depending on position)
    # ----------
    # colors: string[]
    # position: bool
    # fortunes: dictionary<bool, Fortune[]>


    # Fortune
    # ----------
    # identified by specific number
    # contains a textual fortune
    # bonus: populate these from some api or local db randomly
    # ----------
    # number: int
    # fortune: string

# ----------
# how to generate 
# ----------

# randomize from list of colors
# initial position being false (default) is fine
# randomly generate fortunes (for loop: 1-8, alternating positive/negative fortunes)

# ----------
# the game
# ----------

# prompt user for question
# "ok, ill tell you your fortune"
# prompt user for available color
    # validate
# count through length of string, toggling position
# print available numbers
# "choose a number"
    # validate
# print fortune
# ask to play again