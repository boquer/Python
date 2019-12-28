#Se pueden trabajar varias funciones para poder manejar los elementos de las listas.

lista = ["Lunes","Martes",1,3,4,5,5.6,7.5,[7,8,9],"Jueves"]

#Funciones:

lista.append(67) # Me agrega al final de la lista el número 67.
print(lista)
lista.insert(2,"Miercoles") # Me agrega en el índice 2 el día miercoles.
print(lista)
lista.extend(["Viernes","Sábado","Domingo"]) # Me agrega más de dos elementos al final de la lista.
print(lista)
print(lista.index(4)) #Me regresa el valor del índice donde se encuentra el elemento 4.
print(lista.count("Lunes")) #Me imprime cuandos "lunes" se encuentran en la lista.
print(lista.pop()) #Me muestra el último elemento de la lista.
print(lista.pop(1)) #Me muestra el elemento que se encuentra en el índice 1.
lista.remove(1) #Me elimina el número 1 de la lista.
print(lista)
