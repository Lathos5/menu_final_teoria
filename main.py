from typing import  Dict,NoReturn, List
from proyectos.juego_de_la_vida import GameOfLife 
import matplotlib.pyplot as plt
import networkx as nx
import copy
import random
import itertools
import time
import os
G = nx.Graph()
openProy = 0

personalizado = []
conjuntoA = []
conjuntoB = []

print ("--------------------BIENVENIDO AL PROYECTO FINAL---------------------")
print ("------------HECHO POR: ABRAHAM EDUARDO HERNANDEZ FLORES--------------")
print ("\nIngrese el numero correspondiente al proyecto para abrirlo:\n")

"""
</---Funciones de operabilidad de los proyectos
"""
def union_conjuntos(A, B):
    return A.extend(B)

def AUB(A, B):
    return A+B

def AnB(A, B):
    return set(A).intersection(B)

def com(con):
    return set(personalizado).difference(con)

def AdifB(A, B):
    return set(A).difference(B)

def AdifsimB(A, B):
    return set(A).symmetric_difference(B)

def agregar_nodo(origen, destino):
    print(origen)
    print(destino)
    G.add_edge(origen, destino, weight = random.random())

"""
---/>
"""

def startGrafos():

    count = 0
    #lista con letras
    nodes_labels = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]
    #lsta vacia que usaremos para llenarla con los n nodos desde nodes_labels
    actual_nodes = []

    n = int(input("Cuantos nodos desea ingresar?(Hasta 10)\n"))

    for i  in range(len(nodes_labels)):
        count = count + 1
        label = nodes_labels[i]
        actual_nodes.append(label)
        if count == n:
            break
    
    #preguntamos si hay relacion entre los nodos
    for element in actual_nodes:
        print ("Ingrese un 1 si hay relacion con nodo "+element+": ")
        for target in actual_nodes:
            if target == element:
                continue
            relacion = int(input(element+"->"+target+":"))
            if relacion == 1:
                agregar_nodo(element, target)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos = nx.spring_layout(G)  # posiciones para todos los nodos

    # nodos
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # arcos
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # etiquetas
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")
    plt.show()
    
    input('Continuar(Enter)\n\n')

def startConjuntos():

    print ("-------- TEORIA DE CONJUNTOS ---------\n\n")

    liminf = int(input("Ingrese el limite inferior del conjunto Universo (U)\n"))
    limsup = int(input("Ingrese el limite superior del conjunto Universo (U)\n"))


    elemento = 0

    personalizado = list(range(liminf, limsup+1))


    CA = 0

    print("--------- CONJUNTO A-----------\n\n")
    while CA != 'n' :
        CA = input("Ingrese un elemento para {A}. (Salir presione n)\n")
        if CA == 'n':
            break
        conjuntoA.append(int(CA))

    CB = 0

    print("--------- CONJUNTO B-----------\n\n")
    while CB != 'n' :
        CB = input("Ingrese un elemento para {B}. (Salir presione n)\n")
        if CB == 'n':
            break
        conjuntoB.append(int(CB))

    print ("{U}="+ str(personalizado))
    print ("{A}="+ str(conjuntoA))
    print ("{B}="+ str(conjuntoB))

    print("\n\n--------OPERACIONES----------\n\n")
    print("{AuB}: "+str(AUB(conjuntoA, conjuntoB))+"\n")
    print("{AnB}: "+str(AnB(conjuntoA, conjuntoB))+"\n")
    print("{A^c}: "+str(com(conjuntoA))+"\n")
    print("{B^c}: "+str(com(conjuntoB))+"\n")
    print("{A-B}: "+str(AdifB(conjuntoA, conjuntoB))+"\n")
    print("{A/\B}: "+str(AdifsimB(conjuntoA, conjuntoB))+"\n")

    input('Continuar(Enter)\n\n')
def startGameOfLife():

    print("ABRAHAM EDUARDO HERNANDEZ FLORES - 160079")
    for n in range(3):
        print("."*3)

    rows, cols, per, gen = int(input("Rows-> ")), int(input("Cols-> ")), int(input("Porcentaje(30-60)->")), int(input("Numero de generaciones(10 MIN)->"))
    lives = ((rows*cols)*per)/100
    game = GameOfLife(rows, cols, float(lives), True)
        
    print (lives)

    iterations = 0
    while (game.life > 0 or game.dead > 0) and iterations != gen:
        try:        
            game.test()
            print(game)
            print("Iteración N:"+str(iterations))
            time.sleep(3)
            iterations += 1
        except KeyboardInterrupt:
            break
    print("Total: ", iterations)  

    input('Continuar(Enter)\n\n')

while openProy != 4:
    print("1.Grafos")
    print("2.Conjuntos")
    print("3.Juego de la vida")
    print("4.Salir")

    openProy = input("\nSeleccione:")

    if openProy == '1':
        startGrafos()
    elif openProy == '2':
        startConjuntos()
    elif openProy == '3':
        startGameOfLife()
    else:
        break