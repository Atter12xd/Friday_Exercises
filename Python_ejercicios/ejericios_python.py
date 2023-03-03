# Desarrole un algoritmo para hallar el area de un circulo, el usario debe ingresar el radio

import math # Importamos la biblioteca math
print("Ingrese el radio del circulo: ") # ponemos un print para que el usario ponga el radio del circulo 
radio = float(input()) # usamos float para devolver una representacion de coma flotante de el numero.
Area = math.pi * (radio * radio) # calculamos el area 
print("El area del circulo con radio ",radio," Es: ",Area ) # mostramos el area 