import string

frase = input("Ingrese una frase: ")


frase = frase.lower() # Convierto la frase en minúsculas


ocurrencias = {letra: 0 for letra in string.ascii_lowercase} # Creo un diccionario para contar las ocurrencias de cada letra

# Cuento las ocurrencias de cada letra en la frase
for letra in frase:
    if letra.isalpha():
        ocurrencias[letra] += 1

# Imprimo el resultado
for letra, count in ocurrencias.items():
    if count > 0:
        print(f"La letra {letra} aparece {count} vez/veces.")
