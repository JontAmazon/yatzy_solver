"""Helper functions such as:
    - get_sum_upper_section
    - get_final_score
    - roll
    - update_scoreboard
    - EV: get the sum of the upper section, or the difference left to 63?
"""
import random
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


def get_sum_upper_section(scoreboard):
    """(Used to check if the player gets the bonus)."""
    upper_section = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    sum = 0
    for combo, value in scoreboard.items():
        if combo in upper_section:
            sum += value
    return sum


def get_final_score(scoreboard):
    """Calculate the final Yatzy score."""
    # print("[get_final_score]")
    sum = 0
    for combo, value in scoreboard.items():
        if value is None:
            raise ValueError(f"The value for {combo} is None.")
        assert value >= 0
        sum += value
    if get_sum_upper_section(scoreboard) >= 63:
        bprint("Bonus achieved!")
        sum += 50
    else:
        bprint("Bonus not achieved.")
    return sum


def roll(values, save):
    """Roll the dice that are not saved."""
    new_values = values.copy()
    for i, die in enumerate(values):
        if not save[i]:
            new_values[i] = random.randint(1, 6)
    # debug prints:
    print(f"rolling the dies...")
    # print(f"old values: {values}")
    # print(f"save: {save}")
    pprint(f"new_values: {new_values}")
    return new_values


def update_scoreboard(choice, scoreboard):
    """Update the scoreboard with the given choice.

    Example choice: {"full house": 18}
    """
    choicee = next(iter(choice))
    assert scoreboard[choicee] is None
    scoreboard[choicee] = choice[choicee]
