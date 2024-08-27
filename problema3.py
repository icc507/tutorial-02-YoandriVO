#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
t = input().split()
enteros = list(map(int,t))


def insertarArbolTrinario(arbol, t):
    if arbol == []:
        return [t, [], [], []]
    elif t < arbol[0]:
        arbol[1] = insertarArbolTrinario(arbol[1], t)
    elif t == arbol[0]:
        arbol[2] = insertarArbolTrinario(arbol[2], t)
    else:
        arbol[3] = insertarArbolTrinario(arbol[3], t)

    return arbol

def IterarNumerosArbol(t):
    arbol = []
    for numero in t:
        arbol = insertarArbolTrinario(arbol, numero)
    return arbol


arbol_trinario = IterarNumerosArbol(enteros)
print(arbol_trinario)
