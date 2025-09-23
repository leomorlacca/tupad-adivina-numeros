# Juego de adivinanza de numeros binarios y decimales
import random

print("===== Bienvenido/a al juego de adivinanza de numeros binarios! =====")
nombre_jugador = input("Ingresá tu nombre: ")
decimal = None

jugar = "si"

while jugar == "si":
    nivel = 1
    while nivel <= 3:
        if nivel == 1:
            # Generamos un número al azar entre 1 y 9
            decimal = random.randint(1, 9)
        if nivel == 2:
            # Generamos un número al azar entre 10 y 20
            decimal = random.randint(10, 20)
        if nivel == 3:
            # Generamos un número al azar entre 20 y 30
            decimal = random.randint(20, 30)
        
        # Convertimos a binario para luego comparar los resultados
        n = decimal
        binario = ""
        if n == 0:
            binario = "0"
        else:
            while n > 0:
                binario = str(n % 2) + binario
                n //= 2

        # Repetimos hasta que el jugador acierte
        while True:
            respuesta = input(f"{nombre_jugador}, estás en el nivel {nivel}. ¿Cuál es el equivalente en decimal del número binario '{binario}' ? -> ")
            if int(respuesta) == decimal: # Convertimos la respuesta del usuario a int porque input() devuelve un string
                print("¡Correcto!")
                break   # Salimos del while y pasamos al siguiente nivel
            else:
                print("Incorrecto. Probá otra vez.")
        
        # Pasamos al siguiente nivel
        nivel += 1


    # Indicamos la victoria y preguntamos si quiere volver a jugar.
    jugar = input(f"Ganaste, {nombre_jugador}! Superaste los 3 niveles! ¿Te gustaría volver a jugar? (si/no): ")

# El usuario dió fin al juego. Nos despedimos cordialmente.
print(f"Nos vemos pronto {nombre_jugador}!")