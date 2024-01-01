### WEIRD BEHAVIORS --> EV TODOs

# PRIO 1
First turn:
Final values: [1, 4, 6, 6, 6]
final_choice: {'three of a kind': 18}
    - should obviously choose "sixes" here.
    - try lowering costs of upper section when rolls_left == 0.
    - Maybe the cost function needs to consider "values"!
        - yes!
        - but how exactly?


Values: [2, 4, 4, 5, 5]
Saving: [4, 4]
Aiming for: fours
    - It should have aimed for fives. Weighted diffs were very close.
    - Can I simply decrease cost function of fives? (And probably sixes as well)


# PRIO 2



# PRIO 3



# PRIO 4





# ------------------------------------------

MAJOR problem as it should happen very often:
turns_left: 15   <--
 Roll #2
Values: [1, 2, 3, 3, 6]
Saving: [1]
Aiming for: ones
    - tried increasing cost of ones in roll 1 and 2. SURPRISED it didn't work.
        - It didn't increase the average score at least. (In theory it could have fixed this problem but caused another).
    - tried increasing weight of ones. Didn't increase the score.
    - tried reversing the weights when diffs are negative. Lowered the score a lot.
    - worked:
        Added tweek in get_expected_values for ones:
        # Try tweek not to aim for ones:
        if nbr == 1 and count < 2:
            expected_value -= 3
    ... I guess the reason it didn't work to fix it using the cost function or weights, but this worked, was that here I considered "count".
    ... could have done that in cost function as well... but whatever.





