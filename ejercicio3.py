numeros = []
suma = 0

while True:
    numero = int(input("Ingrese un número entero cuando desee terminar seleccione cero: "))
    
    if numero == 0:
        break
    
    numeros.append(numero)
    suma += numero

promedio = suma / len(numeros) if len(numeros) > 0 else 0

print("La lista de números ingresados es:", numeros)
print("La sumatoria de los números es:", suma)
print("El promedio de los números es:", promedio)
