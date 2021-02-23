def niveles():
    #Niveles elevados a la potencia
    n1 = []
    for i in range(6):
        n1.append(pow(20,i))    
    return n1

def maya():
    #La posición 0 = Raya y 1 = Punto
    n2 = []
    for i in range (2):
        n2.append(0)
    return n2

def espacios():
    #Para arreglos de Resultados
    n2 = []
    for i in range(4):
        n2.append(0)
    return n2

#Se asignan los Valores de los Arreglos
nivelista = niveles()
resultados = espacios()
resultados_1 = espacios()

rango = len(resultados)

def maya_res():
    for i in range(rango):
        resultados[i] = maya()

#Crea el arreglo que tiene el otro arreglo adentro
maya_res()

def res():
    for i in range(rango):
        if(resultados[i][0] > 4):
            resultados[i+1][1] = 1
        if(resultados[i][1] > 4):
            resultados[i][0] = 1 

""" resultados[0][1] = 12
resultados[0][0] = 12
resultados[1][0] = 12
resultados[1][1] = 12 """
res()

# print("0 = Raya 1 = Punto \n",resultados)