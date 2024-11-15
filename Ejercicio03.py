numero1 = int(input("Introduce un numero entero y positivo: "))
if numero1 % 2 == 0:
    print(numero1, "es par")
else:
    print(numero1, "es impar")
numero2 = int(input("Dime un numero: "))
lista = []
for i in range(1,numero2 + 1):
    if i % 3 == 0:
        lista.append(i)
print(lista)
