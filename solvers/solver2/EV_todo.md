# PRIO 1
- Förstå varför den valde detta:
turns_left: 15
 Roll #3
Final values: [1, 2, 2, 4, 6]
final_choice: {'ones': 1}
Den borde lagt det på tvåor.
Jag tror att jag kan ändra på cost function eller weights för att undvika att den gör detta dumma

# PRIO 2
- improve straights:
    let "get_expected_scores" take scoreboard as input, and:
    - hard-code: when both small and large straight left, increase expected value of the straights when values have [2,3,4,5].
    - increase expected value of straights when few turns left and nothing important left?
- kolla mer på outputs (leta gömda buggar och värdera hur bra den "tänker")
    - kolla på "expected_scores" för varje kombo (skippa sort?)
    - kolla på dess val.
- solver2: improve two pairs and full house:
    - currently (2023.12.27 kl 16:40), Solver 2 never saves two differt types of dice. For these combos it really should!
    - BRAINSTORM how I could improve expected_score for two pairs and full house!!!


# PRIO 3


