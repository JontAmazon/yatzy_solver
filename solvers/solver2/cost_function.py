"""Solver 2 cost function.

NOTE: The cost function is (kind of) what you aim to get for each combination.
"""
from helper import get_upper_section_diff


BASE_COST_FUNCTION = {
    "ones": 2.1,
    "twos": 4.1,
    "threes": 8,
    "fours": 11,
    "fives": 13,
    "sixes": 16,
    "one pair": 11,
    "two pairs": 15,
    "three of a kind": 12.1,
    "four of a kind": 12.1,
    "small straight": 10,
    "large straight": 10,
    "full house": 16,
    "chance": 25,
    "yatzy": 10,
}


def get_cost_function(scoreboard, rolls_left):
    """Return cost function used by Solver 2."""
    cost_function = BASE_COST_FUNCTION.copy()

    # 1. Decrease costs of ones and twos if plus score in upper section.
    assert cost_function["ones"] == 2.1
    assert cost_function["twos"] == 4.1
    buffer = get_upper_section_diff(scoreboard)
    # Decrease cost of ones
    # But don't aim for ones, so only decrease cost if no rolls left
    if rolls_left == 0:
        for _ in range(2):
            if buffer >= 1 and scoreboard["ones"] is None:
                cost_function["ones"] -= 1
                buffer -= 1
    #elif rolls_left == 2:
    #    cost_function["ones"] += 1  # didn't help
    # Decrease cost of twos
    # But don't aim for twos, so only decrease cost if no rolls left
    if rolls_left == 0:  # tried < 2, didn't help
        for _ in range(2):
            if buffer >= 2 and scoreboard["twos"] is None:
                cost_function["twos"] -= 2
                buffer -= 2

    # 2. Decrease costs over time
    # (could do more continuously, e.g. factor = 0.9 + 0.2 * turns_left/14)
    # (but should maybe start from the middle, e.g. turns_left/7 etc.)
    turns_left = sum(1 for value in scoreboard.values() if value is not None)
    if turns_left < 5:
        cost_function["four of a kind"] -= 2
        cost_function["full house"] -= 2
    if turns_left < 3:
        cost_function["three of a kind"] -= 2
        cost_function["two pairs"] -= 2

    # 3. Generally it's better to discard straights (and sometimes yatzy)
    # than put something suboptimal in the upper section --> QUICK FIX:
    if rolls_left == 0:
        cost_function["small straight"] = 0.11
        cost_function["large straight"] = 0.12
        # cost_function["yatzy"] = 0.13
        # NOTE: keeping it slightly above 0.1, as we decrease the costs for
        # ones and twos to 0.1, if there is a buffer for it (see above). 
        # Future TODO: brainstorm better solutions.
        # Attempts that didn't work:
        if turns_left < 3:
            if scoreboard["sixes"] is None or \
                scoreboard["fives"] is None or \
                scoreboard["fours"] is None or \
                scoreboard["threes"] is None:
                cost_function["yatzy"] = 0.2
                # cost_function["four of a kind"] = 0.3
                # cost_function["full house"] = 0.4

    # 4. Try fixing problem that it chooses three of a kind
    #    when it should choose the upper section.
    #if rolls_left == 0:
    #    cost_function["fives"] = 12.09  # a bit lower than three of a kind
    #    cost_function["sixes"] = 12.09  # a bit lower than three of a kind
        # Something should be done to fix that problem. But...
        # ... maybe it's time to start with Solver 3 or Solver 4 instead.

    return cost_function
        



""" ATTEMPTS THAT DIDN'T WORK:
    if False:
        # A. Adapt to rolls_left. (Didn't work).
        if rolls_left == 2:
            cost_function["three of a kind"] -= 4
            cost_function["four of a kind"] -= 4
        elif rolls_left == 1:
            cost_function["three of a kind"] -= 2
            cost_function["four of a kind"] -= 2
"""