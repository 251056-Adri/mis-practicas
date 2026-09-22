calificaciones = [85, 92, 78, 60, 95, 88, 70, 100, 65, 82, 91, 74, 89, 68, 96]
#--- parte 1: Orden Ascendente ----
ascendente = calificaciones.copy()
n = len(ascendente)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if ascendente[j] > ascendente[j + 1]:
           ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
           swapped = True
    if not swapped:
        break

print("Orden Ascendente:", ascendente)

#--- Parte2: Orden Descendente ---
descendente = calificaciones.copy()
n = len(descendente)

for i  in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if descendente[j] < descendente[j + 1]:
           descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
           swapped = True
    if not swapped:
        break

print("Orden descendente:", descendente)