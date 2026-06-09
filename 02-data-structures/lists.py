"""Exercice de base"""

liste = [12, 15, 8, 19, 14]
p = liste[0]
for i in range(len(liste)):
    if liste[i] > p:
        p = liste[i]
print(f"le plus gros nombre est {p}")

    
"""Exercice bonus"""
        
notes = [12, 15, 8, 19, 14]
total = 0

for note in notes:
    total = total + note

moyenne = total / len(notes)
print(moyenne)

plus = 0
for j in range(len(notes)):
    if notes[j] > moyenne:
        plus = plus + 1
print(f"le nombre de note en dessus de la moyenne est de {plus}")