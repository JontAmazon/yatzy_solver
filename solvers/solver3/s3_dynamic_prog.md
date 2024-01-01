# Allmänt:
När det bara är 1 kast kvar kan man beräkna/estimera saker ganska bra.
När det är 2 kast kvar är det MYCKET svårare.
Idé:
När det är 2 kast kvar kan man testa att slå tärningarna 100 gånger och... eller vänta... VILKA tärningar är frågan... hm... never mind, detta kommer nog tillbaka till dynamisk programmering kom jag på.

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

# Tankar:
- det vore bra om jag gjorde något rekursivt, helst med cache.
- ev. hade jag samtidigt kunnat fortsätta använda konceptet med "cost function" och "weight function".

# EVEVEV:
count;
rolls_left;
5-count stycken nestlade for-loopar.
    I varje for-loop, låt tärningen anta alla värden mellan 1-6.
    I slutet mät antalet kombinationer där vi fick det antal sexor vi behövde, delat på totalt antal kombinationer.
"""


