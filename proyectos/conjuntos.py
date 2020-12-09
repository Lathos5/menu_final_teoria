def union_conjuntos(A, B):
    return A.extend(B)

personalizado = []
conjuntoA = []
conjuntoB = []

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

print("\n\n--------OPERACIONES----------\n\n")
print("{AuB}: "+str(AUB(conjuntoA, conjuntoB))+"\n")
print("{AnB}: "+str(AnB(conjuntoA, conjuntoB))+"\n")
print("{A^c}: "+str(com(conjuntoA))+"\n")
print("{B^c}: "+str(com(conjuntoB))+"\n")
print("{A-B}: "+str(AdifB(conjuntoA, conjuntoB))+"\n")
print("{A/\B}: "+str(AdifsimB(conjuntoA, conjuntoB))+"\n")



