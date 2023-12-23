"""Yatzy Solver attempt 1"""
# ____Definitions____
# Combination: E.g. pair, full house, or chance.
# Turn: A game of Yatzy consists of 15 turns. On each turn, you have 3 rolls.
import json
from helper import roll
from helper import update_scoreboard
from helper import get_final_score
from get_choices import get_choices
from conf_debug import debug_print
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint
from solvers.solver1 import generate_choice
# from solvers.solver2.solver2 import generate_choice


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
    bprint(f"\n\n\n New turn. turns_left: {turns_left}")
    values = [None, None, None, None, None]
    save = [False, False, False, False, False]
    rolls_left = 3
    while rolls_left:
        print(f"\n rolls_left: {rolls_left}")
        values = roll(values, save)
        rolls_left -= 1
        current_choices = get_choices(values, scoreboard)
        final_choice, save = generate_choice(current_choices, scoreboard, values, rolls_left)
        if final_choice:
            update_scoreboard(final_choice, scoreboard)
            rolls_left = 0
    turns_left -= 1
    debug_print(f"\n Updated scoreboard: {scoreboard}")
    # debug_print(f"\n Updated scoreboard: {json.dumps(scoreboard, indent=4)}")
bprint("\n\n Game ended!")
final_score = get_final_score(scoreboard)
bprint(f"Final score: {final_score}")
bprint(f"Final scoreboard:")
print(json.dumps(scoreboard, indent=4))
