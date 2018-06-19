from Vertice import*
from Aresta import*
from Grafo import*
def cria_grafoNO() -> object:
    """

    :rtype: object
    """
    x = int(input("Informe a quantidade de vertices do grafo NÃO ORIENTADO\n"))

    lista = [0 for i in range(x)]
    listaADJ = [['' for i in range(1)] for j in range(x)]
    listaADJOB = [[0 for i in range(1)] for j in range(x)]
    matriz = [[0 for i in range(x)] for j in range(x)]
    print(matriz)
    print(lista)

    dicStN = {}
    dicNtS = {}

    name = input("qual o nome do grafo: \n")

    for i in range(x):

        a = ''
        while(a == ''):
            print("informe os vertices a serem inseridos: (", i + 1, ") de ", x, ":\n")
            a = input()
            vertice = Vertice(a, '', '')
            lista[i] = vertice
            dicStN[a] = i
            dicNtS[i] = a

    for i in range(x):
        for j in range(x):
            if (j <= i):
                print('Existe arestas entre os vertices ', dicNtS[j], ' e ', dicNtS[i], '? (s para sim, qualquer letra para não): ')
                c = input()
                if (c == 's'):
                    matriz[i][j] = Aresta('', '', 1)
                    matriz[j][i] = Aresta('', '', 1)
                else:
                    matriz[i][j] = Aresta('', '', 0)
                    matriz[j][i] = Aresta('', '', 0)

    print(lista)
    print(listaADJ)

    for i in range(len(lista)):
        for j in range(len(lista)):
            arest = matriz[i][j]
            if (arest.num == 1):
                x = dicNtS[i]
                y = dicNtS[j]
                listaADJ[i][0] = x
                listaADJ[i].append(y)
                listaADJOB[i][0] = lista[i]
                listaADJOB[i].append(lista[j])

    new_graf = Grafo(name ,matriz, lista, listaADJ, listaADJOB, dicStN, dicNtS)  # type: Grafo
    print(new_graf.dicStN)

    return new_graf

def verifica_matriz(grafo):
    return grafo.matriz

def verifica_lista(grafo):
    return grafo.lista

def verifica_verticeMATNO(grafo):
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


def verifica_verticeLISTNO(grafo):
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
            print(ver)

    for i in range(len(lista)):
        vert = lista[i]
        g = vert.nome
        if (g == j):
            ver = ver + 1
            y = dicStN[j]
            print(ver)

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


    print(ver)
    if (ver >= 2):
        if (verificador > 0):
            print('VERDADE')
        else:
            print('MENTIRA')
    else:
        print("Um dos vertices inseridos não pertence ao grafo")


def verfica_vertADJLISTA(grafo):
    print("ADJACENCIA POR LISTA")
    lista = grafo.lista
    adj = grafo.listaADJ
    dicStN = grafo.dicStN
    dicNtS = grafo.dicNtS
    ver = 0

    vertice =  str(input('Qual o vertice a ser verificada os vertices adjacentes? \n'))

    for i in range(len(lista)):
        vert = lista[i]
        g = vert.nome
        if (vertice == g):
            ver = ver + 1
            print(ver)

    if (ver > 0):
        for i in range(len(adj)):
            x = dicNtS[i]
            if (x == vertice):
                for j in range(len(adj[i])):
                    if (j > 0):
                        c = adj[i][j]
                        print("Vertices adjacentes a ", vertice,": ", c)
    else:
        print("O VERTICE NÂO EXISTE")



def verfica_vertADJMATRIZ(grafo):
    print("ADJACENCIA POR MATRIZ")
    lista = grafo.lista
    mat = grafo.matriz
    dicStN = grafo.dicStN
    dicNtS = grafo.dicNtS
    ver = 0

    vertice = str(input('Qual o vertice a ser verificada os vertices adjacentes? \n'))

    for i in range(len(lista)):
        vert = lista[i]
        g = vert.nome
        if (g == vertice):
            ver = ver + 1
            print(ver)


    if (ver > 0):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (i == dicStN[vertice]):
                    aresta = mat[i][j]
                    if (aresta.num != 0):
                        c = dicNtS[j]
                        print("Vertices adjacentes a ", vertice, ": ", c)
    else:
        print("O VERTICE NÃO EXISTE")




def imprime_matriz(grafo):
    mat = grafo.matriz
    arestas = [[0 for i in range(len(mat))] for j in range(len(mat))]

    print('Matriz do grafo ', grafo.nome)
    for i in range(len(mat)):
        for j in range(len(mat)):
            arestas[i][j] = mat[i][j].num

    for i in range(len(mat)):
        print(arestas[i])