# PRIO 1
- Spela, spela, spela.
    - kolla om den gör tokiga grejer.
- Try varying the upper section costs over the three rolls.






# PRIO 2
- improve straights:
    - hard-code: when both small and large straight left, increase expected value of the straights when values have [2,3,4,5].
- om det bara är 2 rundor kvar och det bara är e.g. sexor och fyrtal kvar, gissar jag att den inte satsar tillräckligt mycket på sexor.
    - brainstorma/testa nån lösning på detta?


# PRIO 3
- improve straights:
    - let "get_expected_scores" take scoreboard as input, and increase expected value of straights when few turns left and nothing important left?
- improve two pairs and full house:
    - currently (2023.12.27 kl 16:40), Solver 2 never saves two differt types of dice. For these combos it really should!
    - BRAINSTORM how I could improve expected_score for two pairs and full house!!!


# NOTE:
As it currently is, the Solver _will_ do some stupid stuff, _sometimes_.
In order to change it, I would like to change some parameters. But I have gotten to a point where it's very difficult to change some parameters, because they all depend on each other.

# IMPORTANT NOTE:
I think the fundamental implementation has a big flaw when doing this:
    weighted_diffs = diffs * weights
For the combos where diffs is negative, I think one should multiply by 1/weights instead (?). However, when I tried that, the average score decreased a lot. But that is probably because changing it doesn't work with the current parameters, as they are already optimized around this flaw.


