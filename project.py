cat << 'EOF' > project.py
import random

numero_secreto = random.randint(1, 100)
intento = None
intentos = 0
max_intentos = 7

print("¡Bienvenido a Adivina el Número!")
print(f"He pensado un número entre 1 y 100. Tienes {max_intentos} vidas para adivinarlo.")

while intento != numero_secreto and intentos < max_intentos:
    try:
        intento = int(input(f"\nIntento {intentos + 1}/{max_intentos} - Tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")

    except ValueError:
        print("Por favor, escribe un número válido.")

if intento != numero_secreto:
    print(f"\n¡Te quedaste sin vidas! El número secreto era {numero_secreto}.")
EOF