import random

class Personaje:

    def __init__(self, _nombre):
        self.nombre = _nombre
        self.ataque = random.randint(3, 5)
        self.defensa = random.randint(2, 5)
        self.vida = random.randint(10,15)
        self.inventario = []
        self.puntuacion = 0

    def __str__(self):
        cadena = self.nombre + " - Ataque: " + str(self.ataque) + " / Defensa: " + str(self.defensa) \
                 + " [" + str(self.vida) + "]"
        return cadena

