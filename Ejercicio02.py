nombre = input("Dime tu nombre y apellido: ")
nombre,apellido = nombre.split()
print(nombre)
palabra = str(input("Dime una palabra: "))
vocal = str(input("Dime una vocal: "))
palabra = palabra.replace(vocal, vocal.upper())
print(palabra)

