"""
    Módulo Python para ejercicio de comprensión de programas
"""
def insercion(lista):
    """
        Entrada: lista de valores
        Salida: lista de valores ordenados
    """
    for i in range(len(lista)):
        for j in range(i, 0, -1):
            if lista[j-1] > lista[j]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
            else:
                break  

def main():
    """
        Programa principal
    """
    A=[6,5,3,1,8,7,2,4]
    print(A)

    insercion(A)
    print(A)

if __name__ == '__main__':
    main()