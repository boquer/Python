"""Los diccionarios están conformados por elementos desordenados, este acepta dos elementos
por posición (clave y el valor)"""

diccionario = {"azul":"blue","rojo":"red","verde":"green"}#Ejemplo de diccionario.

print(diccionario) #Imprime el diccionario que se tiene.
print("\n",diccionario["azul"])#Muestra el valor de la clave dada.

"""Funciones para los diccionarios"""

diccionario["amarillo"] = "yellow" #Agrega elementos al diccionario.
print("\n",diccionario)#Muestra el nuevo diccionario.

diccionario["azul"] = "BLUE" #modifica elemento del diccionario.
print("\n", diccionario)#Muestra el diccionario modificado.

del(diccionario["verde"])#Elimina los elementos de la clave dada.
print("\n",diccionario)#Imprime el diccionario modificado.
