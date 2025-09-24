# Juego de adivinanza de numeros binarios y decimales
import random
print("====================================================================")
print("===== Bienvenido/a al juego de adivinanza de números binarios! =====")
print("====================================================================")

nombre_jugador = input("Ingresá tu nombre -> ")
decimal = None

jugar = "si"

while jugar == "si":
    nivel = 1
    while nivel <= 3:
        if nivel == 1:
            # Generamos un número al azar entre 0 y 9
            decimal = random.randint(0, 9)
            # Imprimimos el nivel actual
            print(f"{nombre_jugador}, estás en el nivel {nivel}.")
        if nivel == 2:
            # Generamos un número al azar entre 10 y 20
            decimal = random.randint(10, 20)
            # Imprimimos el nivel actual
            print(f"Buenísimo {nombre_jugador}, pasaste al nivel {nivel}.")
        if nivel == 3:
            # Generamos un número al azar entre 20 y 30
            decimal = random.randint(20, 30)
            # Imprimimos el nivel actual
            print(f"{nombre_jugador}, estás en último nivel. Concentración!")
        
        # Convertimos el decimal generado a binario para luego comparar los resultados
        n = decimal
        binario = ""
        if n == 0:
            binario = "0"
        else:
            while n > 0:
                binario = str(n % 2) + binario # Concatenamos los restos y los almaceno en binario
                n //= 2 # Es la version corta de 'n = n // 2'

        # Preguntamos en bucle hasta que el jugador acierte
        while True:
            respuesta = input(f"¿Cuál es el equivalente en decimal del número binario '{binario}' ? -> ")
            if int(respuesta) == decimal: # Convertimos la respuesta del usuario a int porque input() devuelve un string
                print("¡Correcto!")
                break   # Salimos del while y pasamos al siguiente nivel
            else:
                print("Incorrecto. Probá otra vez.")
        
        # Al acertar, pasamos al siguiente nivel
        nivel += 1

    # Indicamos la victoria y preguntamos si quiere volver a jugar.
    print(f"Ganaste, {nombre_jugador}! Superaste los 3 niveles!")
    jugar = input("¿Te gustaría volver a jugar? (si/no) -> ")

# El usuario dió fin al juego. Nos despedimos cordialmente.
print(f"Nos vemos pronto {nombre_jugador}!")