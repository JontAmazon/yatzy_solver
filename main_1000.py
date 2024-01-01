"""Play ~1000 games of Yatzy, and calculate average score, among other statistics."""
import argparse
import json
from helper import roll
from helper import update_scoreboard
from helper import get_final_score
from helper import is_bonus_achieved
from helper import get_choices
import pretty_print

# Choose Solver:
# from solvers.solver1 import generate_choice  # 145 points
from solvers.solver2.solver2 import generate_choice  # 222 points


pretty_print.OMIT_PRINTS = True

parser = argparse.ArgumentParser(description='Play Yatzy thousands of times')
parser.add_argument('--input', '-i', help='Number of games', type=int, default=1000)
args = parser.parse_args()
nbr_games = args.input


scoreboard_all_games = {
    "ones": [],
    "twos": [],
    "threes": [],
    "fours": [],
    "fives": [],
    "sixes": [],
    "one pair": [],
    "two pairs": [],
    "three of a kind": [],
    "four of a kind": [],
    "small straight": [],
    "large straight": [],
    "full house": [],
    "chance": [],
    "yatzy": [], 
}
final_scores = []
bonus_achieved = []

for i in range(nbr_games):
    # print(f"Game {i+1}")
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
        values = 5 * [None]
        save = 5 * [False]
        rolls_left = 3
        while rolls_left:
            values = roll(values, save)
            rolls_left -= 1
            current_choices = get_choices(values, scoreboard)
            final_choice, save = generate_choice(current_choices, scoreboard, values, rolls_left)
            if final_choice:
                update_scoreboard(final_choice, scoreboard)
                rolls_left = 0
        turns_left -= 1
    final_scores += [get_final_score(scoreboard)]
    bonus_achieved += [is_bonus_achieved(scoreboard)]
    # scoreboard_all_games
    for combo, value in scoreboard.items():
        pass

print(f"nbr_games: {nbr_games}")
print(f"final scores average: {sum(final_scores) / nbr_games}")
print(f"fraction bonus achieved: {sum(bonus_achieved) / nbr_games}")

# NOTE: future statistics:
# - histogram for final scores
# - average for each combo
# - histogram for each combo
