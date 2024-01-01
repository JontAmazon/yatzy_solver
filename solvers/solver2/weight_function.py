"""Solver 2 weight function."""

""" NOTE: future improvements:
- take "turns_left" into account? How...? Hm...
- if both small and large straight remain, increase weigh function for both.
- if both two pairs and full house remain, increase weigh function for both.
- let the weight function change over time.
      - after the last roll, increase the prio of:
          - four of a kind, full house, yatzy, and straights
"""

def get_weight_function(scoreboard, rolls_left, bonus_achieved, upper_section_diff):
    """Weight function for Solver 2."""
    weights = {  # 222; 0.67
        "ones": 1,  # 1     hm...
        "twos": 2,   # 2
        "threes": 3,  # 3
        "fours": 3,   # 3
        "fives": 3,   # 3
        "sixes": 3,   # 3
        "one pair": 1,
        "two pairs": 1,
        "three of a kind": 1,
        "four of a kind": 1,
        "small straight": 0.7,
        "large straight": 0.7,
        "full house": 1,
        "chance": 0.5,
        "yatzy": 1,
    }
    if bonus_achieved:
        weights["ones"] = 1
        weights["twos"] = 1
        weights["threes"] = 1
        weights["fours"] = 1
        weights["fives"] = 1
        weights["sixes"] = 1
    
    # Increase weight of three of a kind, because it correlates with many combos
    if rolls_left == 2:
        weights["three of a kind"] = 2
        weights["four of a kind"] = 3
        weights["yatzy"] = 4
    elif rolls_left == 1:
        pass
        # weights["three of a kind"] = 1.5
        # weights["four of a kind"] = 2.25
        # weights["yatzy"] = 2.5

    if rolls_left == 1:
        # Slightly increase weights of rare combinations
        weights["full house"] = 1.2
        weights["four of a kind"] = 1.2

    if rolls_left == 0:
        # Increase weights of rare combinations
        weights["small straight"] = 1.5
        weights["large straight"] = 1.5
        weights["full house"] = 1.5  # effective!!
        weights["four of a kind"] = 1.5
        # weights["yatzy"] = 1.5

    # Take "correlations" into account.
    #if scoreboard["one pair"] is None:
    #    weights["three of a kind"] += 0.4
    #if scoreboard["two pairs"] is None:
    #    weights["three of a kind"] += 0.2
    #if scoreboard["three of a kind"] is None:
    #    weights["four of a kind"] += 1
    # NOTE: Maybe this could work, if tweeked.
    # NOTE: Maybe this could work, if trying again. Fundamentals have changed.
    #       TODO: Try again quickly.

    return weights



""" RESULTS, based on main_1000.py:

# Not good:
elif upper_section_diff >= 5:
    weights["fives"] = 1.5
    weights["sixes"] = 1.5

# Investigate optimal weights:
    if False:  # 216; 0.46
        weights = {
            "ones": 1,
            "twos": 1,
            "threes": 1,
            "fours": 1,
            "fives": 1,
            "sixes": 1,
            "one pair": 1,
            "two pairs": 1,
            "three of a kind": 1,
            "four of a kind": 1,
            "small straight": 1,
            "large straight": 1,
            "full house": 1,
            "chance": 0.5,
            "yatzy": 1,
        }
    if False:  # 222; 0.60
        weights = {
            "ones": 1,
            "twos": 2,    # 2
            "threes": 2,  # 2
            "fours": 2,   # 2
            "fives": 2,   # 2
            "sixes": 2,   # 2
            "one pair": 1,
            "two pairs": 1,
            "three of a kind": 1,
            "four of a kind": 1,
            "small straight": 1,
            "large straight": 1,
            "full house": 1,
            "chance": 0.5,
            "yatzy": 1,
        }
    if False:  # 222.4; 0.674  <-- 67 %
        weights = {
            "ones": 1,
            "twos": 2,    # 2
            "threes": 3,  # 3
            "fours": 3,   # 3
            "fives": 3,   # 3
            "sixes": 3,   # 3
            "one pair": 1,
            "two pairs": 1,
            "three of a kind": 1,
            "four of a kind": 1,
            "small straight": 0.7,
            "large straight": 0.7,
            "full house": 1,
            "chance": 0.5,
            "yatzy": 1,
        }
    if False:  # just upper section --> 161; 0.758
        weights = {
            "ones": 1,
            "twos": 1,  
            "threes": 1,
            "fours": 1, 
            "fives": 1, 
            "sixes": 1, 
            "one pair": 0,
            "two pairs": 0,
            "three of a kind": 0,
            "four of a kind": 0,
            "small straight": 0,
            "large straight": 0,
            "full house": 0,
            "chance": 0,
            "yatzy": 0,
        }
"""