"""Exercice de base"""

nb = int(input("Quel est ton nombre ? "))
if nb % 2 == 0 :
    print("ton nombre est pair")
else:
    print("ton nombre est impair")
    
    
"""Exercice bonus"""
        
nb = int(input("Quel est ton age ? "))
if nb >= 65:
    print("Tu es un senior")
elif nb >= 18:
    print("Tu es un adulte")
elif nb >= 12:
    print("Tu es un adolescent")
else:
    print("Tu es un enfant")
    
    
    
    