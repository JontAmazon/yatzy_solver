"""Solver 2 - Kind of how a human thinks"""
import json
from helper import is_bonus_achieved
from helper import get_upper_section_diff
from pretty_print import debug_print, debug_print2, pprint, bprint
from solvers.solver2.get_expected_scores import get_expected_scores
from solvers.solver2.weight_function import get_weight_function
from solvers.solver2.cost_function import get_cost_function


SOLVER_DESCRIPTION = """
Solver 2 algorithm:
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

NOTES:
- The cost function is (kind of) what you aim to get for each combination.
- The weight function is used because some combinations are more important than others.
For example, it is very important to get lots of fours/fives/sixes in the upper section.
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
    # Algorithm step 1:
    if rolls_left:
        scores, save_dict = get_expected_scores(values, rolls_left)
    else:
        scores = current_choices

    # Check how well we're doing in the upper section
    bonus_achieved = is_bonus_achieved(scoreboard)
    upper_section_diff = get_upper_section_diff(scoreboard)
    cost_function = get_cost_function(scoreboard, rolls_left)
    weight_function = get_weight_function(scoreboard, rolls_left, bonus_achieved, upper_section_diff)

    # Only keep values where scoreboard is None
    scores = {key: value for key, value in scores.items() if scoreboard.get(key) is None}
    cost_function = {key: value for key, value in cost_function.items() if scoreboard.get(key) is None}
    weight_function = {key: value for key, value in weight_function.items() if scoreboard.get(key) is None}

    # Algorithm step 2-4:
    diffs = {key: scores[key] - cost_function[key] for key in scores}
    weighted_diffs = {key: diffs[key] * weight_function[key] for key in diffs}
    choice = max(weighted_diffs, key=weighted_diffs.get)
    # Try "reversing" weights when diffs are negative:
    #weighted_diffs = {
    #    key: (diffs[key] * weight_function[key] if diffs[key] > 0 else diffs[key] * (1 / weight_function[key]))
    #    for key in diffs
    #}  # NOTE: I think this could work super well, but it worked terribly with current parameters.

    # Sorting -> formatting -> printing
    sorted_scores = dict(sorted(scores.items(), key=lambda x: float(x[1])))
    sorted_diffs = dict(sorted(diffs.items(), key=lambda x: float(x[1])))
    sorted_weights = dict(sorted(weighted_diffs.items(), key=lambda x: float(x[1])))
    formatted_scores = {key: format(value, '.4g') for key, value in sorted_scores.items()}
    formatted_diffs = {key: format(value, '.4g') for key, value in sorted_diffs.items()}
    formatted_weights = {key: format(value, '.4g') for key, value in sorted_weights.items()}
    # debug_print2(f"expected_scores: \n {json.dumps(formatted_scores, indent=4)}")
    debug_print(f"(expected?) scores: \n {json.dumps(formatted_scores, indent=4)}")
    # debug_print2(f"diffs: \n {json.dumps(formatted_diffs, indent=4)}")
    debug_print(f"diffs: \n {json.dumps(formatted_diffs, indent=4)}")
    debug_print(f"weighted_diffs: \n {json.dumps(formatted_weights, indent=4)}")

    if rolls_left:
        saved_dice = [value for value, saved in zip(values, save_dict[choice]) if saved]
        pprint(f"Values: {sorted(values)}")
        pprint(f"Saving: {sorted(saved_dice)}")
        pprint(f"Aiming for: {choice}")
        debug_print(f"Expected value: {scores[choice]:.4g}")
        debug_print(f"'Weighted diff': {weighted_diffs[choice]:.4g}")
        debug_print2(f"values (unsorted): {values}")
        debug_print2(f"Saving: {save_dict[choice]}")
        return {}, save_dict[choice]
    else:
        final_choice = {choice: scores[choice]}
        debug_print2(f"Possible choices: \n {json.dumps(current_choices, indent=4)}")
        debug_print(f"Current scoreboard: \n {json.dumps(scoreboard, indent=4)}")
        debug_print(f"Upper section 'status': {upper_section_diff}")
        bprint(f"Final values: {sorted(values)}")
        bprint(f"final_choice: {final_choice}")
        return final_choice, 5 * [True]
