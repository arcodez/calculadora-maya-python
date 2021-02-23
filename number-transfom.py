from convertir import resultados
from number import numeros

niveles = []

cero = 0
punto = 1
raya = 5

#Aun el numero no puedo ser mayor a 19
add = 17

#Definir numeros
def Cero():
    cero = []
    for i in range(4):
        cero.append(0)
    print(cero)

def Punto(add):
    punto = []
    for i in range(add):
        punto.append(".")
    print(punto)
    return punto

def Raya(numr):

    #Esto Hace la raya
    raya = []
    for i in range(4):
        raya.append("=")

    for i in range(numr):
        print(raya)

#Pido un numero
""" add = int(input('Ingrese un número: ')) """

#Se pinta la concha xd
if( add == 0 ):
    Cero()

#Se escribe en puntos si el numero es menor a 5
elif( add < 5):
    resultados[0][1] = add
    Punto(add)

#Aqui se hace la raya que es igual a 5
elif( add == 5 ):
    resultados[0][0] = 1
    Raya(1)

elif( add == 10 ):
    resultados[0][0] = 2
    Raya(2)

elif( add < 10 and add > 5):
    add = add - 5
    resultados[0][1] = add
    resultados[0][0] = 1
    Punto(add)
    Raya(1)

elif( add > 10 and add < 15):
    add = add - 10
    resultados[0][1] = add
    resultados[0][0] = 2
    Punto(add)
    Raya(2)

elif( add > 15 and add < 19):
    add = add - 15
    resultados[0][1] = add
    resultados[0][0] = 3
    Punto(add)
    Raya(3)


print(resultados)