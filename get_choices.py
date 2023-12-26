"""Get the value for each combinations"""
import json
from conf_debug import debug_print, debug_print2
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


def _get_choices(values):
    """Get the value for each combinations.
    
    Do not filter out where the scoreboard is already filled in.
    """
    # debug_print2("[_get_choices]")
    result = {}

    # Upper section:
    result["ones"] = 1 * values.count(1)
    result["twos"] = 2 * values.count(2)
    result["threes"] = 3 * values.count(3)
    result["fours"] = 4 * values.count(4)
    result["fives"] = 5 * values.count(5)
    result["sixes"] = 6 * values.count(6)

    # "one pair", "three of a kind", and "four of a kind":
    max_one_pair = 0
    max_three_of_a_kind = 0
    max_four_of_a_kind = 0
    for i in range(6):
        count = values.count(i)
        if count >= 2:
            max_one_pair = 2 * i
        if count >= 3:
            max_three_of_a_kind = 3 * i
        if count >= 4:
            max_four_of_a_kind = 4 * i

    # "small straight" and "large straight":
    small_straight = 0
    if all(item in values for item in [1, 2, 3, 4, 5]):
        small_straight = 15
    large_straight = 0
    if all(item in values for item in [2, 3, 4, 5, 6]):
        large_straight = 20

    # "two pairs":
    two_pairs = 0
    two_pairs_pair1 = 0
    two_pairs_pair2 = 0
    for i in range(6):
        count = values.count(i)
        if count >= 2:
            if two_pairs_pair1:
                two_pairs_pair2 = 2 * i
            else:
                two_pairs_pair1 = 2 * i
    if two_pairs_pair1 and two_pairs_pair2:
        two_pairs = two_pairs_pair1 + two_pairs_pair2

    # "full house":
    full_house = 0
    full_house_pair_score = 0
    full_house_triplet_score = 0
    for i in range(6):
        count = values.count(i)
        if count == 2:
            full_house_pair_score = 2 * i
        if count == 3:
            full_house_triplet_score = 3 * i
    if full_house_pair_score and full_house_triplet_score:
        full_house = full_house_pair_score + full_house_triplet_score

    # "chance":
    chance = sum(values)

    # "yatzy": 
    yatzy = 0
    for i in range(6):
        count = values.count(i)
        if count == 5:
            yatzy = 50
            print("Yatzy!")

    result["one pair"] = max_one_pair
    result["two pairs"] = two_pairs
    result["three of a kind"] = max_three_of_a_kind
    result["four of a kind"] = max_four_of_a_kind
    result["small straight"] = small_straight
    result["large straight"] = large_straight
    result["full house"] = full_house
    result["chance"] = chance
    result["yatzy"] = yatzy
    return result


def get_choices(values, scoreboard):
    """Get the value for each combinations, except where the scoreboard is already filled in."""
    choices = _get_choices(values)
    debug_print2("[get_choices]")
    for combo, value in scoreboard.items():
        if value is not None:
            del choices[combo]
    bprint(f"Possible choices: {choices}")
    return choices
 