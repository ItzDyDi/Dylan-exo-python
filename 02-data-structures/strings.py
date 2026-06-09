"""Exercice de base"""

lettre = input("Quel est ton mot ? ")
compte = 0

for lettre in lettre:
    if lettre in "aeiouy":  
        compte = compte + 1
    
print(f"le nombre de voyelles est de {compte}")
    
    
"""Exercice bonus"""

phrase = input("Quel est ta phrase ? ")

phrase2 = phrase.split(" ")
print(f"le nombre de mots est de {len(phrase2)}")

mot = phrase2[0]
for i in phrase2:
    if len(i) > len(mot):
        mot = i
print(f"le mot le plus long est '{mot}'")

