
#Se definen los nivel elevados al 20
#El primer nivel inicia en la posición [0]
nivel = []
for i in range(6):
    nivel.append(pow(20,i))    
print(nivel)

numeros = []
for i in range(6):
    numeros.append(0)

#Se dice la cantidad del numero
n = int(170)
print(n)

#Validar que el numero solo llegue hasta el quinto nivel
if( n > 159999):
    print("Solo hasta el 4to nivel")


#Definir en que nivel caen  y descomponer numeros
if(n < 20):
    print("Nivel x 1")
    numeros[0] = n
    print(n)

#Nivel del 20
elif(n < nivel[2] and n > nivel[1]):
    print("Nivel x 20")
    valor = int ((n / nivel[1]))
    res = int (n - (valor*nivel[1]))
    print(valor)
    numeros[1] = valor
    print(res)
    numeros[0] = res

#Nivel del 400
elif(n < nivel[3] and n > nivel[2]):
    print("Nivel x 400")
    valor = int ((n / nivel[2]))
    res = int (n - (valor*nivel[2]))
    n = res
    print(valor)
    numeros[2] = valor

    if(n < nivel[2] and n > nivel[1]):
        valor = int ((n / nivel[1]))
        res = int (n - (valor*nivel[1]))

    print(valor)
    numeros[1] = valor
    print(res)
    numeros[0] = res

#Nivel de 8000
elif(n < nivel[4] and n > nivel[3]):
    print("Nivel x 8.000")
    valor = int ((n / nivel[3]))
    res = int (n - (valor*nivel[3]))
    n = res
    print(valor)
    numeros[3] = valor
    if(n < nivel[3] and n > nivel[2]):
        valor = int ((n / nivel[2]))
        res = int (n - (valor*nivel[2]))
        n = res
        print(valor)
        numeros[2] = valor

        if(n < nivel[2] and n > nivel[1]):
            valor = int ((n / nivel[1]))
            res = int (n - (valor*nivel[1]))
        print(valor)
        numeros[1] = valor
        print(res)
        numeros[0] = res

#Nivel de 160000 al dividir en decimal redondea por lo tanto no funciona como deberia
elif(n < nivel[5] and n > nivel[4]):
    print("Nivel x 160.000")
    valor = int ((n / nivel[4]))
    res = int (n - (valor*nivel[4]))
    n = res
    print(valor)
    if(n < nivel[4] and n > nivel[3]):
        valor = int ((n / nivel[3]))
        res = int (n - (valor*nivel[3]))
        n = res
        print(valor)
        if(n < nivel[3] and n > nivel[2]):
            valor = int ((n / nivel[2]))
            res = int (n - (valor*nivel[2]))
            n = res
            print(valor)
            if(n < nivel[2] and n > nivel[1]):
                valor = int ((n / nivel[1]))
                res = int (n - (valor*nivel[1]))
                print(valor)
                print(res)
                
print(numeros)
