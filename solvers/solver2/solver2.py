"""Solver 2"""
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint

SOLVER_DESCRIPTION = """
Solver 2. Algorithm: \n
1. Call "get_expected_scores": For each combination, get the \n
expected score you would get if aiming solely at that combination. \n
    # NOTE: This function should also return a "save" list for each combination. \n
2. From each combination, subtract "COST_FUNCTION". \n
3. For each combination, multiply with "WEIGH_FUNCTION", since some combinations \n
are more important than others. For example, it is very important to get lots of \n
fours/fives/sixes in the upper section. \n
Hence we get a value for each combination. Call this dict "combination_value". \n

If not rolls_left:
    final_choice = max(combination_value)
elif rolls_left:
    max("combination_value") --> match with "save" from "get_expected_scores"
"""
# TODO: dubbelkolla att "get_expected_score" kan returnera en "save" lista för varje kombo.


# This cost function is (kind of) what you aim to get for each combination.
# NOTE: future improvement: let this change over time.
COST_FUNCTION = {
    "ones": 1,
    "twos": 5,
    "threes": 9,
    "fours": 13,
    "fives": 16,
    "sixes": 19,
    "one pair": 11,
    "two pairs": 18,
    "three of a kind": 15,
    "four of a kind": 15,
    "small straight": 5,
    "large straight": 7,
    "full house": 16,
    "chance": 25,
    "yatzy": 10,
}

# TODO:
"""
- implement: def get_costs(choices)







"""






def generate_choice(current_choices, scoreboard, values, rolls_left):
    """Decide which dice to roll, or make a final choice.

    :param current_choices: Current choices how to update the scoreboard.
    :param scoreboard: State of the scoreboard.
    :param values: Values of the dice, e.g. [1, 3, 5, 6, 6].
    :param rolls_left: Number of rolls left.
    :return tuple: (final_choice, save).
        final_choice: Dict with final choice, e.g. {"one pair": 12}. Empty dict if no final choice.
        save: Which dice to save and roll again, e.g. [True, False, False, True, False].
    """













