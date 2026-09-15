# Crear una lista de números
numeros = [1, 4, 7, 10, 15, 18, 21]

# Lista vacía para guardar los números pares
pares = []

# Recorrer el arreglo con un ciclo for
for n in numeros:
    # Si el residuo de dividir entre 2 es cero, es par
    if n % 2 == 0:
        pares.append(n)

# Mostrar el resultado final
print(pares)  # Muestra: [4, 10, 18]
