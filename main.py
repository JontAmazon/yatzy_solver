"""Play a game of Yatzy using one of the implemented solvers."""
import json
from helper import roll
from helper import update_scoreboard
from helper import get_final_score
from helper import get_choices
from pretty_print import debug_print, debug_print2, pprint, yprint, bprint

# Choose Solver:
# from solvers.solver1 import generate_choice
from solvers.solver2.solver2 import generate_choice

# NOTE: make sure to set OMIT_PRINTS = False, in pretty_print.py


# Init:
turns_left = 15
scoreboard = {
    "ones": None,
    "twos": None,
    "threes": None,
    "fours": None,
    "fives": None,
    "sixes": None,
    "one pair": None,
    "two pairs": None,
    "three of a kind": None,
    "four of a kind": None,
    "small straight": None,
    "large straight": None,
    "full house": None,
    "chance": None,
    "yatzy": None, 
}
while turns_left:
    yprint(f"\n\n\n\n\n New turn. turns_left: {turns_left}")
    yprint(f"_____________________________________________")
    values = 5 * [None]
    save = 5 * [False]
    rolls_left = 3
    while rolls_left:
        pprint(f"\n\n\n Roll #{rolls_left - 2*(rolls_left-2)}")
        values = roll(values, save)
        rolls_left -= 1
        current_choices = get_choices(values, scoreboard)
        final_choice, save = generate_choice(current_choices, scoreboard, values, rolls_left)
        if final_choice:
            update_scoreboard(final_choice, scoreboard)
            rolls_left = 0
    turns_left -= 1
    debug_print2(f"\n Updated scoreboard: {scoreboard}")
    # debug_print2(f"\n Updated scoreboard: {json.dumps(scoreboard, indent=4)}")
# bprint("\n\n Game ended!")
final_score = get_final_score(scoreboard)
bprint(f"Final score: {final_score}")
bprint(f"Final scoreboard:")
print(json.dumps(scoreboard, indent=4))
