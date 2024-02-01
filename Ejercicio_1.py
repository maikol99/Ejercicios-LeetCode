def kids_with_candies(candies, extra_candies):
    result = []  # Esto es lo que vamos a retornar

    for i in range(len(candies)):  # Recorremos el arreglo
        total_candies = candies[i] + extra_candies  # Sumamos los caramelos extras

        # Comparar si total_candies es el valor mayor del arreglo
        greater_value = False
        for j in range(len(candies)):
            if candies[j] > total_candies:
                result.append(False)
                greater_value = True
                break

        if not greater_value:
            result.append(True)

    return result

# Ejemplo de uso
candies = [2, 2, 2, 6, 2]
extra_candies = 3
print(kids_with_candies(candies, extra_candies))  
# Output: [True, True, True, False, True]


