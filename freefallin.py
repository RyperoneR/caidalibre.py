"""
Este programa calcula la posición final de un objeto en caida libre según:
Su altura
Su velocidad inicial
El tiempo transcurrido
"""

#Preguntamos al usuario por la posición inicial
altura = float(input("¿A cuántos metros de altura se encontraba el objeto antes de empezar la medición?: "))

#Preguntamos al usuario por la velocidad inicial
velocidad_inicial = float(input("¿A qué velocidad en metros por segundo iba el objeto antes de empezar la medición?: "))

#Preguntamos al usuario por el valor tiempo
tiempo = float(input("¿Cuántos segundos han transcurrido desde que el objeto está en caida? "))

#Calculamos la posición final del objeto
posicion_final = velocidad_inicial*tiempo-1/2*9.8*(tiempo*tiempo)+altura

#Si la posicion final es negativa significa que ha llegado al suelo por lo tanto eliminamos la posibilidad de que lo sea
if (posicion_final < 0):
    print("El objeto se ha chocado contra el suelo.")
else:
    print("El objeto se encuentra a", posicion_final,"metros de altura.")