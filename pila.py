#Pilas, último en entrar, primero en salir.

pila = [1,2,3]

print("Pila principal ",pila)

pila.append(4) #Función para agregar elementos al final de la pila.
pila.append(5)

print("Pila con el número 4 y 5 agregado: ", pila)

pila.pop()#Función para eliminar el último elemento de la pila.

print("Pila quitando el último elemento ", pila)
