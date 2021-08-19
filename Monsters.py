import random

class Monster:

    def __init__(self):
        self.ataque = random.randint(1,3)
        self.defensa = random.randint(1,2)
        self.vida = random.randint(1,5)

    def __str__(self):
        cadena = "Ataque: " + str(self.ataque) + " / Defensa: " + str(self.defensa) + " [" + str(self.vida)  + "]"
        return cadena