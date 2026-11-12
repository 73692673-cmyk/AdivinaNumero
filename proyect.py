import random

# La computadora elige un número secreto entre 1 y 100
numero_secreto = random.randint(1, 100)
intento = None

print("¡Bienvenido a Adivina el Número!")
print("He pensado un número entre 1 y 100. ¿Cuál es?")

# Bucle principal del juego
while intento != numero_secreto:
    try:
        intento = int(input("Tu número: "))
        
        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
            
    except ValueError:
        print("Por favor, escribe un número válido.")