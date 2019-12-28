#Las tuplas son como listas, la única diferencia es que no se pueden modificar.

tupla = (1,2,3,"Hola",4.5)

#¿Qué se puede hacer con las tuplas?
#Unicamente se pueden visualizar los elementos que esta contiene.

print(tupla) #Muestra todos los elementos que se encuentran en ella.
print(tupla[1]) # Muestra el elementos que se encuentra en el índice 1.
print(tupla.index("Hola")) #Muestra el índice donde se encuentra ese elemento.
print(tupla.count(2)) #Muestra cuantos "2" existen en la tupla.
print(len(tupla)) #Muestra el # de elementos que tiene la tupla.


"""Convirtiendo tuplas el listas"""

tupla = (1,2,3,"Hola",4.5) #Tupla inicial.

lista = list(tupla)#Convierte la tupla en una lista.
print(lista) #Me imprime la lista nueva.



"""Conviertiendo las listas en tuplas"""

lista = [1,2,3,"Hola",4.5] #Lista Inicial.

tupla = tuple(lista) #Convierte la lista en una tupla.
print(tupla) #Me imprime la tupla nueva.
