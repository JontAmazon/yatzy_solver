"""For each combination, get the expected score you would get if aiming solely
   at that combination. Also return a "save" list for each combination.
"""
import json
from helper import get_dice_count_for_value
from conf_debug import debug_print, debug_print2
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


def get_expected_scores(values, rolls_left):
    """For each combination, get the expected score you would get if aiming solely
       at that combination. Also return a "save" list for each combination.
    """
    debug_print("[get_expected_scores]")
    expected_scores = {}
    expected_scores["ones"] = _upper_section(values, rolls_left, 1)
    expected_scores["twos"] = _upper_section(values, rolls_left, 2)
    expected_scores["threes"] = _upper_section(values, rolls_left, 3)
    expected_scores["fours"] = _upper_section(values, rolls_left, 4)
    expected_scores["fives"] = _upper_section(values, rolls_left, 5)
    expected_scores["sixes"] = _upper_section(values, rolls_left, 6)
    
    expected_scores["one pair"] = _one_pair(values, rolls_left)
    expected_scores["three of a kind"] = _three_of_a_kind(values, rolls_left)
    expected_scores["four of a kind"] = _four_of_a_kind(values, rolls_left)
    expected_scores["yatzy"] = _yatzy(values, rolls_left)

    expected_scores["small straight"] = _small_straight(values, rolls_left)
    expected_scores["large straight"] = _large_straight(values, rolls_left)

    expected_scores["two pairs"] = _two_pairs(values, rolls_left)
    expected_scores["full house"] = _full_house(values, rolls_left)
    
    expected_scores["chance"] = _chance(values, rolls_left)

    for combo, value in expected_scores.items():
        if value < 0:
            raise ValueError(f"Expected scores should not be negative (?). \n"
                             f"expected_scores: \n {json.dumps(expected_scores, indent=4)}")
        elif value > 50:
            raise ValueError(f"Expected scores should not be over 50.\n"
                             f"expected_scores: \n {json.dumps(expected_scores, indent=4)}")

    debug_print(f"expected_scores: \n {json.dumps(expected_scores, indent=4)}")
    return expected_scores


# ---------------------------------------------------------------------------------
# --------------   Methods for the individual combinations below   ----------------
# ---------------------------------------------------------------------------------

def _upper_section(values, rolls_left, nbr):
    """Get expected scores in the upper section."""
    debug_print("[_upper_section]")
    count = values.count(nbr)
    debug_print2(f"values: {values}")
    debug_print2(f"nbr of {nbr} in values: {count}")
    if rolls_left == 2:
        expected_value = nbr * (count + 1/6 * (5-count) + 1/6 * 5/6 * (5-count))
    if rolls_left == 1:
        expected_value = nbr * (count + 1/6 * (5-count))
    return expected_value

""" naive approach; independent of rolls_left; for each number:
    calculate the chance of getting a pair. Multiple with the score.
"""
def _one_pair(values, rolls_left):
    """Get expected score for one pair."""
    for i in range(1, 7):
        get_dice_count_for_value(i)    






    
def _three_of_a_kind(values, rolls_left):
    """TODO"""
    
def _four_of_a_kind(values, rolls_left):
    """TODO"""
    
def _yatzy(values, rolls_left):
    """TODO"""


# -------------------------------------------------------------------------

def _small_straight(values, rolls_left):
    """TODO"""
    
def _large_straight(values, rolls_left):
    """TODO"""
    

# -------------------------------------------------------------------------


def _two_pairs(values, rolls_left):
    """TODO"""
    
def _full_house(values, rolls_left):
    """TODO"""


# -------------------------------------------------------------------------


def _chance(values, rolls_left):
    """TODO"""
    







