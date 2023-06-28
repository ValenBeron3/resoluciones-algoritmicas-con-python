
while True:
    print("Menu de Opciones \n")
    print("1 <--Ejercicio positivo negativo y cero")
    print("2 <--Ejercicio Suma de numeros en una lista")
    print("3 <--Ejercicio Ocurrencia de letras")
    print("4 <--Ejercicio Suma de digitos")
    print("5 <--Salir")
    
    opc=int(input("\nIngrese la opcion: "))
    
    if opc==1:
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

    elif opc==2:
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
    
    elif opc==3:
        import string

        frase = input("Ingrese una frase: ")


        frase = frase.lower() # Convierto la frase en minúsculas


        ocurrencias = {letra: 0 for letra in string.ascii_lowercase} # Creo un diccionario para contar las ocurrencias de cada letra

        # Cuento las ocurrencias de cada letra en la frase
        for letra in frase:
            if letra.isalpha():
                ocurrencias[letra] += 1

        #   Imprimo el resultado
        for letra, count in ocurrencias.items():
            if count > 0:
                print(f"La letra {letra} aparece {count} vez/veces.")
    
    elif opc==4:
        numero = int(input("Ingrese un número entero: "))

        suma_digitos = 0

        while numero != 0:
            digito = numero % 10
            suma_digitos += digito
            numero //= 10

        print("La suma de los dígitos es:", suma_digitos)

    elif opc==5:
        break
    else:
        print("OPCION NO VALIDA\n")