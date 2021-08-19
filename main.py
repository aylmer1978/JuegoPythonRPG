import time

from Character import *
from Weapons import *
from Monsters import *
import names

def Dice(lados):
    return random.randint(1,lados)

def LanzamientoCheck(dados, caras):
    aciertos = 0
    for x in range(dados):
        if Dice(caras) > 3:
            aciertos += 1
    return aciertos
    print(f"Has hecho {aciertos} éxitos.")

def Combate(ataque, defensa):
    aciertoAtaque = LanzamientoCheck(ataque, 6)
    aciertoDefensa = LanzamientoCheck(defensa, 6)

    if aciertoAtaque > aciertoDefensa:
        return aciertoAtaque - aciertoDefensa
    else:
        return 0

def CombateMonstruo():
    monstruoCombate = Monster()
    print(f"{monstruoCombate}")

    for i in range(100000):

        ataquePersonaje = Combate(miPersonaje.ataque, monstruoCombate.defensa)
        ataqueMonstruo = Combate(monstruoCombate.ataque, miPersonaje.defensa)
        miPersonaje.vida -= ataqueMonstruo
        monstruoCombate.vida -= ataquePersonaje

        if miPersonaje.vida <= 0:
            print("GAME OVER")
            print(f"{miPersonaje.nombre} ha matado a {miPersonaje.puntuacion} monstruos.")
            break

        if monstruoCombate.vida <= 0:
            print(f"{miPersonaje.nombre} ha matado al monstruo y le quedan {miPersonaje.vida} puntos de vida.\n")
            miPersonaje.puntuacion += 1
            break

        else:
            print(f"{ataquePersonaje} vs {ataqueMonstruo}")

#Con esta función chequeo la media de éxitos de los combates
def TestCombat(ataque, defensa, repeticiones):
    a = 0
    for i in range(repeticiones):
        a = a + Combate(ataque, defensa)
    return a / repeticiones

def crearPersonajes(cantidad):
    opciones = []
    for i in range(cantidad):
        opciones.append(Personaje(names.get_first_name()))
    return opciones

personajes = crearPersonajes(10)

for i in personajes:
    print(f"{personajes.index(i)+1}: {i}")


miPersonaje = personajes[int(input("Elige personaje: "))-1]


#CombateMonstruo()
a = True

while a:
     CombateMonstruo()
     time.sleep(0.3)
     if miPersonaje.vida <= 0:
         a = False



