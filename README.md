# yatzy_solver
Implemented a solver for Scandinavian Yatzy (5 dice, 15 turns, max score is 374).

# Solver 2:
Relies on heuristics, no heavy calculations (so not really a yatzy "solver".) It usually plays well, but makes stupid decisions sometimes.

Algorithm:
1. get expected scores for each combination
2. for each combination, subtract cost function
3. for each combination, multiply by weight function
4. use the max value to determine which dice to save

Average score: 229

Example game - see solvers/solver2/example_game.txt

