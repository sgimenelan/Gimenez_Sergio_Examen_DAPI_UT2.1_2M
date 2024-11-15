paises = []
while len(paises) < 3:
    paises.append(input("Dime un que te gustaria visitar: "))
for i in range(len(paises)):
    print("Me gustaria visitar", paises[i])

numeros = input("Dime una lista de numeros separados por comas:")
numeros = numeros.split(",")
list(map(int,numeros))
print("Numero mas alto:", max(numeros))
print("Numero mas bajo:", min(numeros))

