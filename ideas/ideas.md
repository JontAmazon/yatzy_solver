# Probably start by excluding the bonus
The concept of the bonus makes it a lot more difficult to create a Yatzy solver...

# Always keep the dies you have the most of
A very simple approach that I think would work quite well.

# Fixed cost function
Use a cost function with expected values (sort of), e.g.:
scoreboard = {
    "ones": 1,
    "twos": 5,
    "threes": 9,
    "fours": 13,
    "fives": 17
    "sixes": 20.5
    "one pair": 11.5
    "two pairs": 18,
    "three of a kind": 15,
    "four of a kind": 14.9,
    "small straight": 2,
    "large straight": 2.5,
    "full house": 16,
    "chance": 25,
    "yatzy": 3,
}
    NOTE: how to decide which dice to roll...?

# Fixed cost function that changes every ~3 turns
A simple approach that I think would work quite well: Use a fixed cost function that changes e.g. every third turn.
Example: At the beginning of the game, aim to get 4 sixes/fives for the upper section. Later on, lower your standards.
    NOTE: how to decide which dice to roll...?

# Cost function that depends on the scoreboard
Realistically the cost function would also depend on the scoreboard. Mostly:
    - turns_left
    - bonus_diff (how much is left to get the bonus)
    - bonus_choices_left
But this is quite complex, probably.
    NOTE: how to decide which dice to roll...?

# Brute force -- simulate all permutations
1. rolls_left == 1:
Simulate all permutations of "save".
Calculate the chance of getting each final dice result.
... Idk








