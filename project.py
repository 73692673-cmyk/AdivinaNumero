cat << 'EOF' > project.py
import random
import os

ARCHIVO_RECORD = "record.txt"

def obtener_record():
    if os.path.exists(ARCHIVO_RECORD):
        with open(ARCHIVO_RECORD, "r") as f:
            contenido = f.read().strip()
            if contenido.isdigit():
                return int(contenido)
    return None

def guardar_record(intentos):
    with open(ARCHIVO_RECORD, "w") as f:
        f.write(str(intentos))

print("¡Bienvenido a Adivina el Número!")
record_actual = obtener_record()
if record_actual:
    print(f"Récord actual: {record_actual} intentos.")

# Selección de dificultad (Cambio 2)
print("\nElige una dificultad:")
print("1. Fácil (1 - 50)")
print("2. Medio (1 - 100)")
print("3. Difícil (1 - 500)")

opcion = input("Opción (1/2/3): ").strip()
if opcion == "1":
    limite = 50
elif opcion == "3":
    limite = 500
else:
    limite = 100

numero_secreto = random.randint(1, limite)
intento = None
intentos = 0
max_intentos = 7

print(f"\nHe pensado un número entre 1 y {limite}. Tienes {max_intentos} vidas.")

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
            # Guardar récord (Cambio 3)
            if record_actual is None or intentos < record_actual:
                guardar_record(intentos)
                print("¡Nuevo récord guardado!")

    except ValueError:
        print("Por favor, escribe un número válido.")

if intento != numero_secreto:
    print(f"\n¡Te quedaste sin vidas! El número secreto era {numero_secreto}.")
EOF