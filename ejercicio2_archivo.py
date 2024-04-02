import csv

nombre_archivo = "datos.csv"
anio_usuario = int(input("Ingrese el año para calcular el promedio de los trimestres: "))

with open(nombre_archivo, 'r') as archivo:
    lector = csv.reader(archivo, delimiter= ";")
    
    next(lector, None) 
    
    for fila in lector:
        anio_registro = int(fila[0])
        if anio_registro == anio_usuario:
            trimestre1 = int(fila[1])
            trimestre2 = int(fila[2])
            trimestre3 = int(fila[3])
            trimestre4 = int(fila[4])
            suma_trimestres = sum([trimestre1, trimestre2, trimestre3, trimestre4])
            promedio = suma_trimestres / 4
            print(f"El promedio de los trimestres del año {anio_usuario} es: {promedio}")




#otra forma para llegar a la misma solucion 
# import csv

# nombre_archivo = "datos.csv"
# anio_usuario = int(input("Ingrese el año para calcular el promedio de los trimestres: "))

# with open(nombre_archivo, 'r') as archivo:
#     lector = csv.reader(archivo, delimiter= ";")
    
#     next(lector, None) 
    
#     total_trimestres = 0
#     total_suma_trimestres = 0
    
#     for fila in lector:
#         anio_registro = int(fila[0])
#         if anio_registro == anio_usuario:
#             trimestre1 = int(fila[1])
#             trimestre2 = int(fila[2])
#             trimestre3 = int(fila[3])
#             trimestre4 = int(fila[4])
#             suma_trimestres = trimestre1 + trimestre2 + trimestre3 + trimestre4
#             total_trimestres += 4
#             total_suma_trimestres += suma_trimestres
    
#     if total_trimestres > 0:
#         promedio = total_suma_trimestres / total_trimestres
#         print(f"El promedio de los trimestres del año {anio_usuario} es: {promedio}")
#     else:
#         print(f"No hay registros para el año {anio_usuario}.")
