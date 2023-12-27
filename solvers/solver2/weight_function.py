"""Solver 2 weight function."""

""" NOTE: future improvements:
- take "turns_left" into account? How...? Hm...
- if both small and large straight remain, increase weigh function for both.
- if both two pairs and full house remain, increase weigh function for both.
- let the weight function change over time.
      - after the last roll, increase the prio of:
          - four of a kind, full house, yatzy, and straights
- let the weights in the upper section depend on helper.get_upper_section_status?
"""

def get_weight_function(rolls_left, bonus_achieved, upper_section_status):
    """Weight function for Solver 2."""

    # Default values:
    weights = {
        "ones": 0.3,
        "twos": 0.6,
        "threes": 1,
        "fours": 1.2,
        "fives": 2.5,  # quite large
        "sixes": 4,    # very large
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

    if bonus_achieved:
        weights["fives"] = 1
        weights["sixes"] = 1

    elif upper_section_status >= 5:
        weights["fives"] = 1.5
        weights["sixes"] = 1.5

    if rolls_left == 0:
        # Increase weights of rare combinations
        weights["small straight"] = 1.7
        weights["large straight"] = 1.7
    
    return weights
