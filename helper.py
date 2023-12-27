"""Helper functions such as:
    - get_sum_upper_section
    - roll
    - get_final_score
    - update_scoreboard
    - get_choices
    - get_upper_section_status
"""
import random
from conf_debug import debug_print, debug_print2
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


def get_sum_upper_section(scoreboard):
    """(Used to check if the player gets the bonus)."""
    upper_section = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    sum = 0
    for combo, value in scoreboard.items():
        if combo in upper_section:
            if scoreboard[combo]:
                sum += value
    return sum


def is_bonus_achieved(scoreboard):
    """Return True if bonus has already been achieved."""
    return get_sum_upper_section(scoreboard) >= 63


def roll(values, save):
    """Roll the dice that are not saved."""
    new_values = values.copy()
    for i, die in enumerate(values):
        if not save[i]:
            new_values[i] = random.randint(1, 6)
    # debug prints:
    # print(f"rolling the dies...")
    # print(f"old values: {values}")
    # print(f"save: {save}")
    pprint(f"Values: {sorted(new_values)}")
    return new_values


def get_final_score(scoreboard):
    """Calculate the final Yatzy score."""
    # print("[get_final_score]")
    sum = 0
    for combo, value in scoreboard.items():
        if value is None:
            raise ValueError(f"The value for {combo} is None.")
        assert value >= 0
        sum += value
    if is_bonus_achieved(scoreboard):
        bprint("\n\n\nBonus achieved!  :)")
        sum += 50
    else:
        bprint("\n\n\nBonus not achieved.  =(")
    return sum


def update_scoreboard(choice, scoreboard):
    """Update the scoreboard with the given choice.

    Example choice: {"full house": 18}
    """
    choicee = next(iter(choice))
    assert scoreboard[choicee] is None
    scoreboard[choicee] = choice[choicee]


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
    for i in range(1, 7):
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
    for i in range(1, 7):
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
    for i in range(1, 7):
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
    for i in range(1, 7):
        count = values.count(i)
        if count == 5:
            yatzy = 50
            for i in range(10):
                yprint("Yatzy!")

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
    debug_print2(f"Possible choices: {choices}")
    return choices


def get_upper_section_status(scoreboard):
    """Get a number representing how well the upper section is going.

    A positive value means the upper section is going well.

    Note: The bonus is achieved is getting a sum of 63, corresponding to 3 of each number.
    Therefore, this method can be used to get a "status" for how the upper section is going.
    
    NOTE: Not sure how/if I could use this method though... we'll see...
    NOTE: Draft. Un-used method.
    """
    status_for_nbrs = []
    for i, (combo, _) in enumerate(scoreboard.items()):
        nbr = i + 1
        if nbr <= 6:
            if scoreboard[combo] is not None:
                status_for_nbrs += [scoreboard[combo] - (3*nbr)]
    print(f"status_for_nbrs: {status_for_nbrs}")
    print(f"sum: {sum(status_for_nbrs)}")  # OK if empty?
    return sum(status_for_nbrs)
    
    # NOTE: Future improvements:
    # - also look at how many turns are left.

