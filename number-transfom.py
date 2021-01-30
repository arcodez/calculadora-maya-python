
#Pido un numero
add = int(input('Ingrese un número: '))

#Se pinta la concha xd
if( add == 0 ):
    cero = []
    for i in range(4):
        cero.append(0)

#Se escribe en puntos si el numero es menor a 5
elif( add < 5):
    n = []
    for i in range(add):
        n.append(".")
    print(n)

#Aqui se hace la raya que es igual a 5
elif( add == 5 ):
    raya = []

    for i in range(add):
        raya.append("=")

    print(raya)

elif( add == 10 ):
    n = np.array(raya)


else:
    print("El numero es diferente de 5")


