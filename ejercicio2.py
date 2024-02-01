def stepsandnumbers(num):
    pasos = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            print("El numero es par")
            print("División actual:", num)
        else: 
            num = num - 1
            print("El numero es impar")
            print("División actual:", num)
        pasos += 1
            
print(stepsandnumbers(14))

