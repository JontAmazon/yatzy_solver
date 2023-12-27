# PRIO 1
- git rm ideas/ideas.md?
- Solver 2: verifiera att avg score ökade av att jag ökade cost function för chance till 27.
- Solver 2: testa öka cost function för ettorna till 2.1. Men minska till 0.1 om ligger plus 2 i upper section. Liknande för 2:orna. 
- Solver 2: öka weight för tretal i runda 1 och 2?
- Solver 2: om par, tretal och två-par finns kvar, öka weight för fyrtal!
- Solver 2: om par och två-par finns kvar, öka weight för tretal!

- Solver2: Nåt är fel med trissen. Borde nog behålla cost function, men öka prio! Exempel stupid decision:
 New turn. turns_left: 3
 Roll #1
Values: [1, 4, 4, 6, 6]
Values: [1, 4, 4, 6, 6]
Saving: [6, 6]
Aiming for: three of a kind
 Roll #2
Values: [2, 3, 3, 6, 6]
Values: [2, 3, 3, 6, 6]
Saving: [2, 3]
Aiming for: small straight

- Solver 2: Förstå varför den valde detta:
 New turn. turns_left: 13
    (Den har redan fått femmor (och ettor)).
 Roll #1
Values: [1, 1, 5, 5, 6]
Saving: [6]
Aiming for: one pair
Borde naturligtvis satsa på 5or för att få förhoppningsvis fyrtal, och alternativt par, tretal, tvåpar, kåk...
    - EV TODO: printa weighted diffs för just detta.
    - idé: om par, tretal och två-par finns kvar, öka weight för fyrtal! osv.

- Solver 2: Förstå varför den valde detta:
turns_left: 15
 Roll #3
Final values: [1, 2, 2, 4, 6]
final_choice: {'ones': 1}
Den borde lagt det på tvåor.
Jag tror att jag kan ändra på cost function eller weights för att undvika att den gör detta dumma

# PRIO 2
- Solver 2: printa upper section när den misslyckas med bonusen. Kolla hur det brukar se ut. Kanske borde öka cost function för ettorna till 3, om den brukar misslyckas pga dem?

- Solver 3 -- dynamisk programmering:
    - rekursiv metod

- Solver 4 -- använda Solver 2 rekursivt?
    - Låt Solver 2 ta fram "save" för varje kombo, sedan för varje "save"-kandidat spela 100 partier (icke-rekursivt) och se score.
    - Detta skulle kunna fixa problem med bonusen (?).




# LATER



# EV
- gärna refaktorisera koden --> klass "yatzy_data" för att representera all data.




# EVEVEV
- Later: Maxi yatzy?
