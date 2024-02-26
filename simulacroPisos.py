matriz = []
opcion = 1

for i in range(4):
    matriz.append([0] * 6)

print("DEPARTAMENTOS A, B, C, D")

for i in range(4):
    print(matriz[i])

try:
    while opcion != 0:
        fila = int(input("Ingrese el numero de la fila que quiera:"))
        columna = int(input("Ingrese el numero de la columna que quiera:"))
        habitantes = int(input("Ingrese el numero de habitantes de su vivienda:"))
        
        
        matriz[fila - 1][columna - 1] += habitantes

        print("Las viviendas cargadas hasta el momento son estas")
        for i in range(4):
            print(f"{i + 1} - {matriz[i]}")

        opcion = int(input("¿Deseas seguir agregando? Presiona 0 para salir - 1 para continuar\n"))

  
    piso_mas_habitantes = 0
    piso_menos_habitantes = 0
    max_habitantes = sum(matriz[0])
    min_habitantes = sum(matriz[0])

    for i in range(1, 4):
        habitantes_piso_actual = sum(matriz[i])
        
        if habitantes_piso_actual > max_habitantes:
            max_habitantes = habitantes_piso_actual
            piso_mas_habitantes = i

        if habitantes_piso_actual < min_habitantes:
            min_habitantes = habitantes_piso_actual
            piso_menos_habitantes = i

    print(f"\nEl piso con más habitantes es el {piso_mas_habitantes + 1} con {max_habitantes} habitantes.")
    print(f"El piso con menos habitantes es el {piso_menos_habitantes + 1} con {min_habitantes} habitantes.")

    for i in range(4):
        total_habitantes_piso = sum(matriz[i])
        media_habitantes_piso = total_habitantes_piso / 6
        print(f"La media de habitantes en el piso {i + 1} es: {media_habitantes_piso}")
        
    
    # Encontrar la vivienda (piso y depto) con más habitantes
    max_habitantes_vivienda = matriz[0][0]
    piso_max_habitantes_vivienda = 1
    depto_max_habitantes_vivienda = 1

    for i in range(4):
        for j in range(6):
            if matriz[i][j] > max_habitantes_vivienda:
                max_habitantes_vivienda = matriz[i][j]
                piso_max_habitantes_vivienda = i + 1
                depto_max_habitantes_vivienda = j + 1

    print(f"La vivienda con más habitantes es en el piso {piso_max_habitantes_vivienda}, departamento {depto_max_habitantes_vivienda} con {max_habitantes_vivienda} habitantes.")

except ValueError:
    print("Ingrese un dato valido")
