# PRIO 2
- improve straights:
    let "get_expected_scores" take scoreboard as input, and:
    - hard-code: when both small and large straight left, increase expected value of the straights when values have [2,3,4,5].
    - increase expected value of straights when few turns left and nothing important left?
- kolla mer på outputs (leta gömda buggar och värdera hur bra den "tänker")
    - kolla på "expected_scores" för varje kombo (skippa sort?)
    - kolla på dess val.


# PRIO 3
Som det är nu (2023.12.27 kl 16:40) kommer Solver 2 aldrig att spara på två olika typer av tärningar, vilket nog hade varit bra i vissa fall, tex här:
    turns_left: 15
 Roll #1
Values: [1, 3, 4, 5, 6]
Här KANSKE den borde spara på både 5 och 6, men sparar bara på 6an. Men det lär inte göra så stor skillnad i det här fallet.
Däremot när det kommer till tvåpar och kåk!!



