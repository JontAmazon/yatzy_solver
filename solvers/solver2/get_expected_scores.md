### Brainstorm "get_expected_score"

# straights:
    if rolls_left == 2:
        if nbr_matching < 4:
            expected_value = 0  # don't aim for a straight
        if nbr_matching == 5:
            expected_value = 25  # exagerate expected value
        if nbr_matching == 4:
            chance_5_matching = 1 - 5/6 * 5/6
            expected_value = 15 * chance_5_matching
            expected_value *= 0.75  # usually better not to go for straights

    if rolls_left == 1:
        chance_5_matching = math.prod(i / 6 for i in range(nbr_missing))
        expected_value = 15 * chance_5_matching
        expected_value *= 0.9  # usually better not to go for straights


# ---------------------------------------------------------------------------------
# ----------------   TRASH   ------------------------------------------------------
# ---------------------------------------------------------------------------------

# full house
- only keep threes, fours, fives and sixes.
- if no pairs or triplets, only keep the fives and sixes.
- maybe this is too complicated, try to re-use two-pair logic instead, but multiply with a factor?


# small straight -- incorrect.
    if rolls_left == 2:
        nbr_matching;
        nbr_missing;
        expected_nbr_matching = average of:
            chance_that_nbr_matching == 1,
            chance_that_nbr_matching == 2, ...
            chance_that_nbr_matching == 5
        these can be calculated as follows:
        chance_5_matching = sum((nbr_missing - i) / 6) for i in range(nbr_missing))
        chance_4_matching = sum((nbr_missing - i + 1) / 6) for i in range(nbr_missing))
        chance_3_matching = sum((nbr_missing - i + 1) / 6) for i in range(nbr_missing))
        chance_2_matching = sum((nbr_missing - i + 1) / 6) for i in range(nbr_missing))
        chance_1_matching = sum((nbr_missing - i + 1) / 6) for i in range(nbr_missing))

        om jag har 0 matchande tärningar får jag 0 matchande om jag får:
            1/6 ^ 5
        om jag har 0 matchande tärningar får jag 1 matchande om jag får:
            1/6 ^ 4 * 5/6
        om jag har 0 matchande tärningar får jag 2 matchande om jag får:   nja... lite fel?
            1/6 ^ 3 * 5/6 * 4/6


    if rolls_left == 1:
        chance_5_matching = sum((nbr_missing - i) / 6) for i in range(nbr_missing))  # incorrect as well.
        expected_value = 15 * chance_5_matching

        factors = []

    (inte trash):
    if rolls_left == 1:
        om jag har 0 matchande tärningar får jag liten stege om jag får:
            5/6 * 4/6 * 3/6 * 2/6 * 1/6
        om jag har 1 matchande tärningar får jag liten stege om jag får:
            4/6 * 
