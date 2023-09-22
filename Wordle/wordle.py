import random


class Palabra:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado


class Categoria:
    def __init__(self, nombre, palabras):
        self.nombre = nombre
        self.palabras = [Palabra(p[0], p[1]) for p in palabras]


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos_restantes = 6
        self.intentos = []

    def hacer_intento(self, palabra):
        self.intentos.append(palabra)
        self.intentos_restantes -= 1


class Juego:
    def __init__(self, jugador, categoria):
        self.jugador = jugador
        self.categoria = categoria
        self.palabra_objetivo = self.seleccionar_palabra()
        self.palabra_adivinada = None

    def seleccionar_palabra(self):
        return random.choice(self.categoria.palabras).palabra

    def proporcionar_retroalimentacion(self, palabra):
        if len(palabra) != len(self.palabra_objetivo):
            return "La palabra debe tener exactamente {} letras.".format(len(self.palabra_objetivo))

        feedback = []
        for i in range(len(self.palabra_objetivo)):
            if palabra[i] == self.palabra_objetivo[i]:
                feedback.append("verde")
            elif palabra[i] in self.palabra_objetivo:
                feedback.append("amarillo")
            else:
                feedback.append("gris")
        return feedback

    def jugar(self):
        print("¡Bienvenido a Wordle!")
        print(f"Categoría: {self.categoria.nombre}")
        print(
            f"Tienes {self.jugador.intentos_restantes} intentos para adivinar una palabra de {len(self.palabra_objetivo)} letras.")
        print("Las letras pueden repetirse en la palabra oculta.\n")

        while self.jugador.intentos_restantes > 0:
            intento = input("Ingresa tu palabra: ").lower()
            feedback = self.proporcionar_retroalimentacion(intento)

            if intento == self.palabra_objetivo:
                self.palabra_adivinada = intento
                print("\n¡Felicidades, {}! Has adivinado la palabra correcta: {}".format(self.jugador.nombre,
                                                                                         self.palabra_adivinada))
                break

            print("Retroalimentación:", feedback)
            self.jugador.hacer_intento(intento)
            print("Intentos restantes:", self.jugador.intentos_restantes)

        if not self.palabra_adivinada:
            print("\n¡Agotaste todos los intentos! La palabra correcta era '{}'.".format(self.palabra_objetivo))
            print("Significado de la palabra: {}".format(self.obtener_significado(self.palabra_objetivo)))

        print("\nFin del juego.")

    def obtener_significado(self, palabra):
        for p in self.categoria.palabras:
            if p.palabra == palabra:
                return p.significado
        return "Significado no encontrado."


class Sistema:
    def __init__(self):
        self.categorias = [
            Categoria("Animales", [
                ("perro", "Animal doméstico de compañía."),
                ("gato", "Animal felino domesticado."),
                ("elefante", "Mamífero terrestre de gran tamaño."),
                ("tigre", "Felino grande y carnívoro."),
                ("ballena", "Mamífero marino de gran tamaño."),
                ("delfín", "Mamífero marino inteligente."),
                ("tortuga", "Reptil de caparazón."),
                ("cebra", "Animal rayado de la sabana africana."),
                ("jirafa", "Mamífero de largo cuello."),
                ("panda", "Oso de peluche en blanco y negro."),
            ]),
            Categoria("Frutas", [
                ("manzana", "Fruta comestible de piel fina."),
                ("plátano", "Fruto de cáscara amarilla."),
                ("sandía", "Gran fruto de pulpa roja."),
                ("uva", "Pequeñas frutas en racimo."),
                ("mango", "Fruta tropical de sabor dulce."),
                ("fresa", "Pequeña fruta roja."),
                ("cereza", "Fruta pequeña y roja."),
                ("piña", "Fruta tropical con cáscara dura."),
                ("kiwi", "Fruta verde con interior suave."),
                ("limón", "Fruta amarilla y ácida."),
            ]),
            Categoria("Países", [
                ("españa", "País ubicado en Europa."),
                ("argentina", "Nación en América del Sur."),
                ("japón", "Nación insular en Asia."),
                ("francia", "País conocido por su gastronomía."),
                ("australia", "Nación rodeada de océanos."),
                ("canadá", "País con vastos paisajes naturales."),
                ("italia", "País famoso por su cocina y arte."),
                ("méxico", "Nación en América del Norte."),
                ("brasil", "País tropical en América del Sur."),
                ("alemania", "Nación europea con industria avanzada."),
            ]),
            # Agregar más categorías y palabras aquí
        ]

    def mostrar_categorias(self):
        print("\nCategorías disponibles:")
        for i, categoria in enumerate(self.categorias):
            print(f"{i + 1}. {categoria.nombre}")

    def ejecutar(self):
        nombre_jugador = input("Ingresa tu nombre: ")

        self.mostrar_categorias()

        while True:
            try:
                opcion = int(input("Selecciona una categoría (1-{}): ".format(len(self.categorias))))
                if 1 <= opcion <= len(self.categorias):
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingresa un número válido.")

        categoria_seleccionada = self.categorias[opcion - 1]

        jugador = Jugador(nombre_jugador)
        juego = Juego(jugador, categoria_seleccionada)
        juego.jugar()


if __name__ == "__main__":
    sistema = Sistema()
    sistema.ejecutar()