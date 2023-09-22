Desarrollo juego Wordle 

Wordle es un juego de palabras en el que el jugador debe adivinar una palabra oculta de cinco
letras en un número limitado de intentos. El juego proporciona retroalimentación después de cada
intento, lo que permite al jugador deducir las letras correctas y su posición dentro de la palabra.
Reglas del juego:
1. Palabra oculta: Al comienzo del juego, se genera aleatoriamente una palabra oculta de cinco
letras. Las letras pueden repetirse, lo que significa que una misma letra puede aparecer en
diferentes posiciones de la palabra.
2. Intentos: El jugador tiene un número limitado de intentos para adivinar la palabra oculta.
Generalmente, se asignan seis intentos, pero este número puede variar según la
implementación del juego. Cada palabra que el jugador ingrese, debe ser una palabra válida
(debe hacer parte de la base de datos de palabras del juego).
3. Retroalimentación: Después de cada intento, el juego proporciona retroalimentación al
jugador. La retroalimentación consiste en indicar cuántas letras del intento son correctas y
están en la posición correcta (marcadas en verde), cuántas letras son correctas, pero están en
una posición incorrecta (marcadas en amarillo) y cuántas letras no hacen parte de la palabra
(marcadas en gris).
4. Lógica y deducción: Basándose en la retroalimentación recibida después de cada intento, el
jugador debe usar su lógica y deducción para reducir las posibilidades y adivinar la palabra
oculta. Al analizar las letras y su posición, se pueden descartar letras incorrectas y buscar
patrones para encontrar la solución correcta.
5. Intentos restantes: El juego muestra el número de intentos restantes para motivar al jugador a
adivinar la palabra antes de agotar los intentos disponibles.
6. Victoria o derrota: El jugador gana el juego si adivina la palabra oculta dentro de los intentos
asignados. En caso contrario, si se agotan todos los intentos sin adivinar correctamente la
palabra, se considera una derrota. En este último caso, el juego muestra cual era la palabra
correcta.
Al finalizar, el jugador tiene la opción de buscar el significado de la palabra (ya sea que la haya
adivinado o no) y de iniciar un nuevo juego.
En cualquier momento, el jugador podrá ver las instrucciones del juego. Además, también deberá
tener la opción de ver las estadísticas del juego donde se le mostrará un gráfico con la distribución
de sus los intentos en cada juego realizado.