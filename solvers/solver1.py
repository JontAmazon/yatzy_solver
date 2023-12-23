"""Solver 1"""
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


SOLVER_DESCRIPTION = """
solver1.py -- very simple solver: \n
- always roll again if 1, 2, or 3 \n
- for the final choice: \n
\t- choose the option with the max score \n
\t- if multiple options give the same max score, use constant 'ORDER_OF_PREFERENCE' \n
"""
print(SOLVER_DESCRIPTION)


ORDER_OF_PREFERENCE = [
    "yatzy", 
    "large straight",
    "small straight",
    "one pair",
    "two pairs",
    "full house",
    "ones",
    "twos",
    "threes",
    "fours",
    "fives",
    "sixes",
    "three of a kind",
    "four of a kind",
    "chance",
]


def get_max_of_current_choices(current_choices):
    """Get choice with the maximum value.
    
    If multiple options give the same max score, use constant 'ORDER_OF_PREFERENCE'.
    """
    choice = None
    max_value = -1
    for combo in ORDER_OF_PREFERENCE:
        if combo in current_choices:
            if current_choices[combo] > max_value:
                max_value = current_choices[combo]
                choice = combo
    return {choice: max_value}


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
    print("[generate_choice]")
    if rolls_left:
        save = [value > 3 for value in values]
        final_choice = {}
        saved_dice = [value for value, saved in zip(values, save) if saved]
        print(f"Choosing to save: {save}")
        pprint(f"Choosing to save: {saved_dice}")
        return final_choice, save
    
    print("No rolls left, choosing the option with the max score.")
    final_choice = get_max_of_current_choices(current_choices)
    save = 5 * [True]
    pprint(f"values: {values}")
    pprint(f"final_choice: {final_choice}")
    return final_choice, save
