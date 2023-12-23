### BRAINSTORM "get_expected_score" FOR ALL COMBINATIONS.

# upper section:
    if rolls_left == 2:
        expected_value = 4 * (count + 1/6 * (5-count) + 1/6 * 5/6 * (5-count))
    if rolls_left == 1:
        expected_value = 4 * (count + 1/6 * (5-count))

# one pair:
    naive approach; independent of rolls_left; for each number:
        calculate the chance of getting a pair. Multiple with the score.
"three of a kind": same as one pair.
"four of a kind": same as one pair.
"yatzy":         same as one pair.

# small straight:
(large straight similar)
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

# two pairs:
- only keep fours, fives and sixes.
- if have a two pair, lock it in.
- if have a pair, keep it, and keep the highest one of the others, if have one.
    - calculate expected value...

Example: pair of fives, nothing else.
if rolls_left == 1:
    expected_value = 2*5 + 3  # arbitrary
if rolls_left == 2:
    expected_value = 2*5 + 6  # arbitrary

Example: pair of fives, one six.
if rolls_left == 1:
    chance_getting_it = 1 - (5/6)**2
    sum = blabla
    expected_value = sum * chance_getting_it

if rolls_left == 2:
    chance_getting_it = 1 - (5/6)**4
    sum = blabla
    expected_value = sum * chance_getting_it

# full house:
- only keep fours, fives and sixes.
- if have a full house, lock it in.
- if have a two pair, calculate !!!
- if have a pair, keep it, and keep the highest one of the others, if have one.
    - calculate expected value, but multiply with some factor probably... probably less than 

# chance: 
    if rolls_left == 2:
        keep fives and sixes. The rest will become 4.25. (Because half of the rest will become 4/5/6 == 5, and half of the rest will become 3.5).
    if rolls_left == 1:
        keep fours, fives, and sixes. The rest will become 3.5.

# ---------------------------------------------------------------------------------
# ----------------   one pair ------------------------------------------------------
# ---------------------------------------------------------------------------------
For each number, calculate the chance of getting a pair. Multiple with the score.

Four scenarios:
1. I need 1 six.
    1a. 1 roll left.
    1b. 2 rolls left.
2. I need 2 sixes.
    2a. 1 roll left.
    2b 2 rolls left.

# Simons feedback 1: Nestlade for-loopar.
Visst blir det en binomialfördelning.
Men programmatiskt är det kanske enklare att göra nestlade for-loopar:
Om det är N kast kvar och 3 tärningar kvar blir det nog 3 for-loopar,
och vi skulle kunna beräkna att sannolikheten för en viss tärning att bli en sexa är X.
Men låt istället varje tärning anta alla värden mellan 1-6, och kör 3 nestlande for-loopar.
Och i slutet mät antalet kombinationer där vi fick det antal sexor vi behövde, delat på
totalt antal kombinationer.

# Simon feedback 2: Brute force, dynamisk programmering.
Man har nån slags rekursiv metod som tar som input (values, rolls_left).
Metoden kallar på sig själv, ... och gör vad exakt?
Jag tror att den testar att rulla om alla olika kombinationer, och därefter anropar sig själv med den nya inputen.
Metoden sorterar values såklart.
Metoden kastar kanske bort vissa inputs.
Metoden cachar outputs för vissa inputs.

# Simons tips 3:
Brute force med rekursiv kod, samt 5 for-loopar från 0 till 1, vilka representerar om tärningen ska sparas eller inte.

# SLUTSATS:
- det vore bra om jag gjorde något rekursivt, helst med cache.
- men jag hade först kunnat försöka göra nåt enkelt med nestlade for-loopar för att försöka göra enkla estimat av expected score för att testa min Solver 2, med dess "cost function". Det hade varit nice att se vad den fick för scores.
    Dock har jag också two_pair kvar...
    Och vision work...? :)
    Kanske borde börja med det istället....
    ..... vi får se vad jag har lust med imorgon......
    ..... men det vore absolut bra! :)










































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
