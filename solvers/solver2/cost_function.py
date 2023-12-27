"""Solver 2 cost function.

NOTE: The cost function is (kind of) what you aim to get for each combination.
"""


def get_cost_function():
    """Return cost function used by Solver 2."""
    # NOTE: smaller numbers => smaller costs
    return BASE_COST_FUNCTION  # 222
    # return SMALLER_UPPER_SECTION  # 219
    # return LARGER_UPPER_SECTION  # 218.5



# First cost function
BASE_COST_FUNCTION = {
    # "ones": 1, "twos": 4,  # 221.7; 0.572 (2023.12.28 kl 15)
    "ones": 3, "twos": 4,  # 221.6; 0.565   (2023.12.28 kl 15)
    "threes": 7,
    "fours": 10,
    "fives": 12,
    "sixes": 15,
    "one pair": 11,
    "two pairs": 18,
    "three of a kind": 15,
    "four of a kind": 15,
    "small straight": 10,
    "large straight": 9.9,
    "full house": 16,
    "chance": 27,
    "yatzy": 10,
}






""" RESULTS from main_1000.py:

# Not good:
SMALLER_UPPER_SECTION = BASE_COST_FUNCTION.copy()
SMALLER_UPPER_SECTION["ones"] = 0
SMALLER_UPPER_SECTION["twos"] = 3
SMALLER_UPPER_SECTION["threes"] = 6
SMALLER_UPPER_SECTION["fours"] = 9
SMALLER_UPPER_SECTION["fives"] = 11
SMALLER_UPPER_SECTION["sixes"] = 14

# Not good:
LARGER_UPPER_SECTION = BASE_COST_FUNCTION.copy()
LARGER_UPPER_SECTION["ones"] = 2
LARGER_UPPER_SECTION["twos"] = 5
LARGER_UPPER_SECTION["threes"] = 8
LARGER_UPPER_SECTION["fours"] = 11
LARGER_UPPER_SECTION["fives"] = 13
LARGER_UPPER_SECTION["sixes"] = 16
"""

