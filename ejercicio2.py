


while True:
    numero = input("Ingrese un número entero cuando desee terminar seleccione asterisco (*) para salir: ")
    
    if numero == '*':
        print("¡Terminamos!")
        break
    
    numero = int(numero)
    
    if numero > 0:
        print("El número ingresado es positivo.")
    elif numero < 0:
        print("El número ingresado es negativo.")
    else:
        print("El número ingresado es igual a cero.")
