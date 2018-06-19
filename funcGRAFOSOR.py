from Vertice import*
from Aresta import*
from Grafo import*

def cria_grafoOR() -> object:
    """

    :rtype: object
    """

    name = input("qual o nome do grafo: ")
    x = int(input("Informe a quantidade de vertices do grafo ORIENTADO\n"))

    lista = [0 for i in range(x)]
    listaADJ = [['' for i in range(1)] for j in range(x)]
    listaADJOB = [[0 for i in range(1)] for j in range(x)]
    matriz = [[0 for i in range(x)] for j in range(x)]
    print(matriz)
    print(lista)

    dicStN = {}
    dicNtS = {}

    for i in range(x):
        a = str(input("informe os vertices a serem inseridos\n"))
        vertice = Vertice(a, '', '')
        lista[i] = vertice
        dicStN[a] = i
        dicNtS[i] = a

    for i in range(x):
        for j in range(x):

            print('Existe arestas saindo do vertice ', dicNtS[j], ' para o vertice ', dicNtS[i], '? (s para sim, qualquer letra para não): ')
            c = input()
            if (c == 's'):
                s = int(input('Qual o peso da aresta: '))
                matriz[i][j] = Aresta('', '', s)
            else:
                matriz[i][j] = Aresta('', '', 0)


    print(lista)
    print(listaADJ)

    for i in range(len(lista)):
        for j in range(len(lista)):
            arest = matriz[i][j]
            if (arest.num != 0):
                x = dicNtS[i]
                y = dicNtS[j]
                listaADJ[i][0] = x
                listaADJ[i].append(y)
                listaADJOB[i][0] = lista[i]
                listaADJOB[i].append(lista[j])
    print(listaADJ)
    print(listaADJOB)


    new_graf = Grafo(name,matriz, lista, listaADJ, listaADJOB, dicStN, dicNtS)  # type: Grafo
    print(new_graf.dicStN)

    return new_graf

def verifica_verticeMATOR(grafo):
    print("VERIFICAÇÃO POR MATRIZ:")
    print("Insira os vertices para serem verificados:")
    i = str(input())
    j = str(input())
    mat = verifica_matriz(grafo)
    dicStN = grafo.dicStN
    dicNtS = grafo.dicNtS
    lista = grafo.lista
    ver = 0
    x = y = 0

    for z in range(len(lista)):
        vert = lista[z]
        g = vert.nome
        if (g == i):
            ver = ver + 1
            print('a', ver)
            print(dicNtS)
            x = dicStN[i]

    for i in range(len(lista)):
        vert = lista[i]
        g = vert.nome
        if (g == j):
            ver = ver + 1
            print('b', ver)
            y = dicStN[j]

    print(ver)
    aresta = mat[x][y]
    if (ver >= 2):
        if (aresta.num != 0):
            print('VERDADE')
        else:
            print('MENTIRA')
    else:
        print("Um dos vertices inseridos não pertence ao grafo")

def verifica_verticeLISTOR(grafo):
    print("VERIFICAÇÃO POR LISTA:")
    print("Insira os vertices para serem verificados:")
    i = str(input())
    j = str(input())
    mat = verifica_matriz(grafo)
    dicStN = grafo.dicStN
    dicNtS = grafo.dicNtS
    lista = grafo.lista
    listaADJ = grafo.listaADJ
    ver = 0
    verificador = 0
    x = y = 0

    for z in range(len(lista)):
        vert = lista[z]
        g = vert.nome
        if (g == i):
            ver = ver + 1
            x = dicStN[i]

    for i in range(len(lista)):
        vert = lista[i]
        g = vert.nome
        if (g == j):
            ver = ver + 1
            y = dicStN[j]

    for i in range(len(mat)):
        if (x == i ) :
            tam = len(listaADJ[i])

            for j in range(tam):
                print(listaADJ[i])
                test = listaADJ[i][j]
                m = dicNtS[y]
                if (m == test)and (j > 0):
                    verificador = verificador + 1
                    print(verificador)


    if (ver >= 2):
        if (verificador > 0):
            print('VERDADE')
        else:
            print('MENTIRA')
    else:
        print("Um dos vertices inseridos não pertence ao grafo")




def verifica_matriz(grafo):
    return grafo.matriz


def verifica_lista(grafo):
    return grafo.lista