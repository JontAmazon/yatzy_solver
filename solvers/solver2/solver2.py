"""Solver 2"""
import json
from conf_debug import debug_print, debug_print2
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint
# from get_expected_scores import get_expected_scores
# from solvers.solver2 import get_expected_scores  # why is this needed...?
from solvers.solver2.get_expected_scores import get_expected_scores


SOLVER_DESCRIPTION = """
Solver 2 algorithm: \n
1. if rolls_left:
        get_expected_scores -> {combination: (score, save)}
   else:
        get_choices         -> {combination: score}
2. for each combination, subtract "COST_FUNCTION".
3. for each combination, multiply with "WEIGHT_FUNCTION"
4. if rolls_left:
        use the max value to get "save".
    else:
        use the max value to make a final choice.
"""


COST_FUNCTION = {
    "ones": 1,
    "twos": 4,
    "threes": 7,
    "fours": 10,
    "fives": 12,
    "sixes": 15,
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
# The cost function is (kind of) what you aim to get for each combination.
#    NOTE: future improvements:
# - let this change over time.


WEIGHT_FUNCTION = {
    "ones": 0.3,
    "twos": 0.6,
    "threes": 1,
    "fours": 1.2,
    "fives": 2.5,
    "sixes": 4,
    "one pair": 0.6,
    "two pairs": 1,
    "three of a kind": 2,
    "four of a kind": 1.5,
    "small straight": 0.45,
    "large straight": 0.55,
    "full house": 1.5,
    "chance": 0.3,
    "yatzy": 2,
}
# The weight function is used because some combinations are more important than others.
# For example, it is very important to get lots of fours/fives/sixes in the upper section.
#   NOTE: future improvements:
# - if both two pairs and full house remain, increase weigh function for both.
# - if both small and large straight remain, increase weigh function for both.
# - define two different weight functions for the two rolls.
# - let the weight function change over time.
#   - when the bonus has been achieved.


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
    if rolls_left:
        scores, save_dict = get_expected_scores(values, rolls_left)
    else:
        scores = current_choices

    # only look at values where scoreboard is None
    scores = {key: value for key, value in scores.items() if scoreboard.get(key) is None}
    cost = {key: value for key, value in COST_FUNCTION.items() if scoreboard.get(key) is None}
    weight = {key: value for key, value in WEIGHT_FUNCTION.items() if scoreboard.get(key) is None}

    # calculate differences, diffs = {key: scores[key] - COST_FUNCTION[key] for key in scores}
    diffs = {key: scores[key] - cost[key] for key in scores}
    weighted_diffs = {key: diffs[key] * weight[key] for key in diffs}
    choice = max(weighted_diffs, key=weighted_diffs.get)

    debug_print(f"expected_scores: \n {json.dumps(scores, indent=4)}")
    debug_print(f"diffs: \n {json.dumps(diffs, indent=4)}")
    debug_print(f"weighted_diffs: \n {json.dumps(weighted_diffs, indent=4)}")

    if rolls_left:
        pprint(f"Choosing: {choice}")
        pprint(f"Expected value: {scores[choice]}")
        pprint(f"'Weighted diff': {weighted_diffs[choice]}")
        saved_dice = [value for value, saved in zip(values, save_dict[choice]) if saved]
        debug_print(f"Choosing to save: {save_dict[choice]}")
        pprint(f"Choosing to save: {saved_dice}")
        return {}, save_dict[choice]
    else:
        bprint("No rolls left. ")
        final_choice = {choice: scores[choice]}
        bprint(f"values: {values}")
        bprint(f"final_choice: {final_choice}")
        return final_choice, 5 * [True]
