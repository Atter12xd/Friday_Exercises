# Desarrollar un algoritmo donde permita el ingreso de datos

numeros = input("Ingrese los numeros: ") # Solicitamos numero al usuario
numeros = [int(numero) for numero in numeros.split(",")] # Convertimos cadena de texto en una lista de numeros
lista_cadenas = list(map(str, numeros)) # hacemos el proceso para convertir los numeros en "list"
print("el de la list son", lista_cadenas) # mostramos la lista

numeros = input("Ingrese los numeros: ") # Solicitamos numero al usuario
numeros = [int(numero) for numero in numeros.split(",")]  # Convertimos cadena de texto en una lista de numeros
lista_cadenas = tuple(map(str, numeros)) # hacemos el proceso para convertir los numeros en "tuple"
print("el de tuple son: ",lista_cadenas) # mostramos el tuplee