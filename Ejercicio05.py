def area_cuadrado(L):
    """Funcion que calcula el area de un cuadrado
    
    Parametros:
        -L = lado del cuadrado
    Salida:
        -un numero real con el area del cuadrado
        con el lado especificado
        """
    return L * L
lado = float(input("Dime el lado del cuadrado: "))
print("El area del cuadrado es", area_cuadrado(lado))

def mayor_de_tres(a, b, c):
    """Funcion que calcula el mayor de 3 numeros
    
    Parametros:
        -a, b, c = 3 numeros reales
    Salida:
        -el numero real mas alto
        """
    return max(a, b, c)
n = []
while len(n) < 3:
    n.append(input("Introduce un numero: "))
print("El numero mayor es", mayor_de_tres(n[0], n[1], n[2]))