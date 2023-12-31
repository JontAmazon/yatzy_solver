# PRIO 1
- Spela, spela, spela.
    - kolla om den gör tokiga grejer.

# PRIO 2
- improve straights:
    - hard-code: when both small and large straight left, increase expected value of the straights when values have [2,3,4,5].


# PRIO 3
- improve straights:
    - let "get_expected_scores" take scoreboard as input, and increase expected value of straights when few turns left and nothing important left?
- improve two pairs and full house:
    - currently (2023.12.27 kl 16:40), Solver 2 never saves two differt types of dice. For these combos it really should!
    - BRAINSTORM how I could improve expected_score for two pairs and full house!!!


# NOTE:
As it currently is, the Solver _will_ do some stupid stuff, _sometimes_.
In order to change it, I would like to change some parameters. But I have gotten to a point where it's very difficult to change some parameters, because they all depend on each other.

