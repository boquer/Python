numero = int(input("Digite un número: "))

if numero>0: #Si el número es mayor a cero, imprime lo de abajo.
    print("El número que ingresó es positivo")


#Si el número no es mayor a cero, pasa a elif

elif numero==0:#Si el número es igual a cero, imprime lo de abajo.
    print("El número que ingresó es cero")

#Si no se cumplieron ningunas de las condiones pasadas, pasa al else

else:
    print("El número que ingresó es negativo")

print("\nFin del programa")
