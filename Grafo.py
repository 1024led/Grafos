from Vertice import*
from Aresta import*

class Grafo:
    nome = ''
    lista = [0 for i in range (0)]
    matriz = [[0 for i in range(0)] for j in range(0)]
    listaADJ = [[0 for i in range(0)] for j in range(0)]
    listaADJOB = [[0 for i in range(0)] for j in range(0)]
    dicStN = {}
    dicNtS = {}

    def __init__(self, nome, matriz, lista, listaADJ, listaADJOB, dicStN, dicNtS):
        self.nome = nome
        self.matriz = matriz
        self.lista = lista
        self.listaADJ = listaADJ
        self.listaADJOB = listaADJOB
        self.dicStN = dicStN
        self.dicNtS = dicNtS







