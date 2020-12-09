'''
Necesitamos las librerias matplotlib y networkx
Podemos instalarlo desde el cmd con py pip
'''

import matplotlib.pyplot as plt
import networkx as nx
import random

G = nx.Graph()

count = 0
#lista con letras
nodes_labels = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]
#lsta vacia que usaremos para llenarla con los n nodos desde nodes_labels
actual_nodes = []

n = int(input("Cuantos nodos desea ingresar?(Hasta 10)\n"))

#agregamos cada nodo al grafo, junto con su destino y grosor de arco
def agregar_nodo(origen, destino):
    print(origen)
    print(destino)
    G.add_edge(origen, destino, weight = random.random())

#agregamos a los nodos actuales desde las labels
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