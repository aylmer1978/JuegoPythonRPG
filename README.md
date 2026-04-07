# JuegoPythonRPG

Juego de rol por consola hecho en Python. El jugador elige un personaje generado aleatoriamente y combate en bucle contra monstruos hasta morir.

## Como funciona

- Se generan 10 personajes con nombre y stats aleatorios
- El jugador elige uno
- El personaje combate automáticamente contra monstruos uno tras otro
- El combate usa un sistema de dados: se lanzan N dados de 6 caras y cada resultado mayor a 3 cuenta como un éxito
- Gana quien consiga más éxitos netos (ataque - defensa)
- El juego termina cuando el personaje muere, mostrando cuántos monstruos eliminó

## Como ejecutarlo

```bash
pip install names
python main.py
```

## Archivos

| Archivo | Descripción |
|---|---|
| `main.py` | Lógica principal: bucle de combate y selección de personaje |
| `Character.py` | Clase `Personaje` con nombre, ataque, defensa y vida |
| `Monsters.py` | Clase `Monster` con stats aleatorios |
| `Weapons.py` | Clase `Arma` (en desarrollo) |

## Dependencias

- [`names`](https://pypi.org/project/names/) — genera nombres aleatorios para los personajes

## Posibles mejoras

### Correcciones menores
- **`print` inalcanzable en `LanzamientoCheck`** — hay un `print` después del `return` que nunca se ejecuta. Eliminarlo.
- **`Weapons.py` sin conectar** — la clase `Arma` existe pero no se usa en el combate. Conectarla o eliminarla.
- **`from X import *`** — sustituir por imports explícitos (`from Character import Personaje`) para evitar conflictos y mejorar la legibilidad.

### Mejoras jugables
- **Regeneración de vida** — el personaje acumula daño sin recuperarse. Recuperar algo de vida al matar un monstruo haría el juego más equilibrado.
- **Nombres para los monstruos** — usar una lista (`["Goblin", "Esqueleto", "Orco"]`) y elegir uno al azar para que el combate sea más descriptivo.
- **Dificultad progresiva** — escalar los stats de los monstruos según la puntuación del personaje para que el juego sea más desafiante con el tiempo.

### Ampliaciones posibles
- **Sistema de armas** — la clase `Arma` y el atributo `inventario` en `Personaje` ya están definidos. Solo faltaría conectarlos al combate.
- **Menú entre combates** — preguntar al jugador si quiere continuar, descansar (recuperar vida) o ver sus stats en lugar del bucle automático.
