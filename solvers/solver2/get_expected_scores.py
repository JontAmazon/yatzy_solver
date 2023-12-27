"""For each combination, get the expected score you would get if aiming solely
   at that combination. Also return a "save" list for each combination.
"""
import math
import json
from conf_debug import debug_print, debug_print2
from pretty_print import pprint, rprint, gprint, yprint, bprint, cprint


def get_indices(value, values):
    return [x == value for x in values]


def get_expected_scores(values, rolls_left):
    """For each combination, get the expected score you would get if aiming solely
       at that combination. Also return a "save" list for each combination.
    """
    debug_print2("[get_expected_scores]")
    expected_scores = {}  # each entry should be a tuple of length 2
                          # with expected score and a "save" list.
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

    for combo, item in expected_scores.items():
        assert isinstance(item, tuple) and len(item) == 2, f"Invalid tuple for {combo}: Tuple: {item}"
        expected_score, save = item
        assert isinstance(expected_score, (int, float)), f"Expected score for {combo} should be a number"
        assert isinstance(save, list) and len(save) == 5 and all(isinstance(val, bool) for val in save), \
            f"Invalid save list for {combo}"
        if expected_score < 0:
            raise ValueError(f"Expected scores should not be negative (?). \n"
                             f"expected_scores: \n {json.dumps(expected_scores, indent=4)}")
        elif expected_score > 50:
            raise ValueError(f"Expected scores should not be over 50.\n"
                             f"expected_scores: \n {json.dumps(expected_scores, indent=4)}")

    expected_scores_values = {key: value[0] for key, value in expected_scores.items()}
    save_dict = {key: value[1] for key, value in expected_scores.items()}
    return expected_scores_values, save_dict


# ---------------------------------------------------------------------------------
# --------------   Methods for the individual combinations below   ----------------
# ---------------------------------------------------------------------------------


def _upper_section(values, rolls_left, nbr):
    """Get expected scores in the upper section."""
    debug_print2(f"[_upper_section], nbr {nbr}")
    count = values.count(nbr)
    debug_print2(f"values: {values}")
    debug_print2(f"nbr of {nbr} in values: {count}")
    if rolls_left == 2:
        expected_value = nbr * (count + 1/6 * (5-count) + 1/6 * 5/6 * (5-count))
    if rolls_left == 1:
        expected_value = nbr * (count + 1/6 * (5-count))
    return expected_value, get_indices(nbr, values)


def _expected_score_x_of_a_kind(values, rolls_left, required_number):
    """Expected score for one pair, three of a kind, four of a kind, and Yatzy."""
    expected_score_max = 0
    for i in range(1, 7):
        count = values.count(i)
        expected_count_increase = rolls_left * 1/6 * (5-count)
        expected_count = count + expected_count_increase
        expected_chance = (expected_count / required_number)**2  # OK...?
        expected_chance = min(1, expected_chance)
        expected_score = i * required_number * expected_chance  # (a bit inaccurate for Yatzy)
        if expected_score > expected_score_max:
            expected_score_max = expected_score
            save = get_indices(i, values)
    return expected_score_max, save


def _one_pair(values, rolls_left):
    return _expected_score_x_of_a_kind(values, rolls_left, 2)

def _three_of_a_kind(values, rolls_left):
    return _expected_score_x_of_a_kind(values, rolls_left, 3)

def _four_of_a_kind(values, rolls_left):
    return _expected_score_x_of_a_kind(values, rolls_left, 4)

def _yatzy(values, rolls_left):
    return _expected_score_x_of_a_kind(values, rolls_left, 5)

    
# -------------------------------------------------------------------------


def _straight(values, rolls_left, type):
    "Expected score for straights."
    if type == "small":
        straight = [1, 2, 3, 4, 5]
        points_for_straight = 15
    else:
        straight = [2, 3, 4, 5, 6]
        points_for_straight = 20

    nbr_matching = sum(1 for nbr in straight if nbr in values)

    if rolls_left == 1:
        chance_5_matching = math.prod(i / 6 for i in range(5 - nbr_matching))
        expected_value = chance_5_matching * points_for_straight
        expected_value *= 0.9  # usually better not to go for straights

    elif rolls_left == 2:
        if nbr_matching < 4:
            expected_value = 0  # don't aim for a straight
            save = 5 * [False]
        elif nbr_matching == 5:
            expected_value = 50  # exaggerate expected value
        elif nbr_matching == 4:
            chance_5_matching = 1 - 5/6 * 5/6
            expected_value = points_for_straight * chance_5_matching
            expected_value *= 0.75  # usually better not to go for straights

    # Save unique dice in "straight":
    save = 5 * [False]
    already_saved = []
    for nbr in straight:
        for i, value in enumerate(values):
            if value == nbr and nbr not in already_saved:
                save[i] = True
                already_saved += [nbr]
    return expected_value, save


def _small_straight(values, rolls_left):
    """Expected score for small straight."""
    return _straight(values, rolls_left, "small")
    
def _large_straight(values, rolls_left):
    """TODO later"""
    return _straight(values, rolls_left, "large")


# -------------------------------------------------------------------------


def _two_pairs(values, rolls_left):
    """Expected score for two pair.
    
    Note: if rolling a pair of sixes and one five, this method would re-roll the five, so it's quite stupid sometimes.
    """
    two_pair = get_two_pair(values)
    if two_pair[0]:
        # Two pair exists -> lock it in!
        return two_pair

    if rolls_left == 2:
        # Too complicated. Assume rolls_left == 1, but multiply result by circa 1.3
        MAX_TWO_PAIR = 22
        expected_score, save = _two_pairs(values, 1)
        expected_score = min(MAX_TWO_PAIR, 1.3 * expected_score)
        return expected_score, save

    # -------- rolls_left == 1 --------
    # Usually only threes, fours, fives and sixes are interesting.
    count3 = values.count(3)
    count4 = values.count(4)
    count5 = values.count(5)
    count6 = values.count(6)
    count = max([count3, count4, count5, count6])

    # Sixes are the most interesting, so check those first.
    if count6 >= 2:
        nbr = 6
    elif count5 >= 2:
        nbr = 5
    elif count4 >= 2:
        nbr = 4
    elif count3 >= 2:
        nbr = 3

    if count >= 2:
        score_of_first_pair = 2 * nbr
        # Always re-roll the other three, yielding:
        average_pair_value = 7.
        chance_of_getting_a_pair = 2/6
        expected_score = score_of_first_pair + chance_of_getting_a_pair * average_pair_value
        save = get_indices(nbr, values)

        if count == 3:  # three of a kind
            # just save two out of the three
            if save[0]:
                save[0] = False
            elif save[1]:
                save[1] = False
            elif save[2]:
                save[2] = False

        elif count == 4:  # four of a kind
            # just save two out of the four
            if save[0]:
                save[0] = False
            elif save[1]:
                save[1] = False
            if save[4]:
                save[4] = False
            elif save[3]:
                save[3] = False

    else:  # count == 1 or count == 0
        expected_score = 10  # completely arbitrary
        save = 5 * [False]
    
    return expected_score, save

    
def _full_house(values, rolls_left):
    """Expected score for full house."""
    full_house = get_full_house(values)
    if full_house[0]:
        return full_house

    two_pair = get_two_pair(values)
    if two_pair[0]:
        # Two pair exists -> easy to calculate expected value for full house.
        two_pair_score, save = two_pair
        full_house_score = 5/4 * two_pair_score
        chance = rolls_left / 6
        expected_score = full_house_score * chance
        return expected_score, save

    # Otherwise it's too complicated -> Return the expected score of a two pair,
    # multiplied by 0.8 because full house is way more difficult to get.
    expected_score, save = _two_pairs(values, rolls_left)
    return 0.8 * expected_score, save


# -------------------------------------------------------------------------


def _chance(values, rolls_left):
    """Expected score for chance."""
    if rolls_left == 2:
        # Keep fives and sixes. The other dice become 4.25.
        # (Because half of the rest will become 4/5/6 == 5, and half of the rest will become 3.5).
        count5 = values.count(5)
        count6 = values.count(6)
        expected_score = count5 * 5 + count6 * 6 + (5-count5-count6) * 4.25
        indices5 = get_indices(5, values)
        indices6 = get_indices(6, values)
        indices = [x or y for x, y in zip(indices5, indices6)]
        return expected_score, indices

    if rolls_left == 1:
        # Keep fours, fives, and sixes. The rest will become 3.5.
        count4 = values.count(4)
        count5 = values.count(5)
        count6 = values.count(6)
        expected_score = count4 * 4 + count5 * 5 + count6 * 6 + (5-count4-count5-count6) * 3.5
        indices4 = get_indices(4, values)
        indices5 = get_indices(5, values)
        indices6 = get_indices(6, values)
        indices = [x or y or z for x, y, z in zip(indices4, indices5, indices6)]
        return expected_score, indices


# ---------------------------------------------------------------------------------
# --------------   Help methods    ------------------------------------------------
# ---------------------------------------------------------------------------------


def get_two_pair(values):
    """Get the value of any two pair, and the indices of those dice."""
    valid_nbrs = [2, 3, 4, 5, 6]  # omit ones, too low score...
    nbr_pair1 = None
    nbr_pair2 = None
    for nbr in valid_nbrs:
        count = values.count(nbr)
        if count >= 2:
            if nbr_pair1 is None:
                nbr_pair1 = nbr
            else:
                nbr_pair2 = nbr
    if nbr_pair1 and nbr_pair2:
        two_pair_value = 2 * (nbr_pair1 + nbr_pair2)
        indices1 = get_indices(nbr_pair1, values)
        indices2 = get_indices(nbr_pair2, values)
        indices = [x or y for x, y in zip(indices1, indices2)]
    else:
        two_pair_value = 0
        indices = 5 * [False]
    return two_pair_value, indices


def get_full_house(values):
    """Get the value of any full house, and the indices of those dice."""
    valid_nbrs = [1, 2, 3, 4, 5, 6]
    nbr_triplet = None
    nbr_pair = None
    for nbr in valid_nbrs:
        count = values.count(nbr)
        if count == 3:
            nbr_triplet = nbr
        elif count == 2:
            nbr_pair = nbr
    if nbr_triplet and nbr_pair:
        full_house_value = 3 * nbr_triplet + 2 * nbr_pair
        indices = 5 * [True]
    else:
        full_house_value = 0
        indices = 5 * [False]
    return full_house_value, indices

