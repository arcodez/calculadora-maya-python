n1 = 2 
n2 = 3

def Suma():
    for i in range(len(resultados)):
        resultados[i][1] = resultados[i][1] + resultados_1[i][1]
        resultados[i][0] = resultados[i][0] + resultados_1[i][0]
        return resultados

def Resta():
     return n1 - n2

def Multiplicacion():
    return n1 * n2

def Division():
    if(n2 == 0):
        print("No se puede dividir entre 0")
    else:    
        return n1 / n2

# print(Suma())
