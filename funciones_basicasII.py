# Cuenta regresiva
def cuentaRegresiva(num):
    arr = []
    entry = 0
    entry = int(input('Ingrese numero para cuenta regresiva: '))

    for i in range(entry, 0, -1):
        arr.append(i)

    print(arr)
cuentaRegresiva(5)

# Imprimir y volver
def imprimirVolver(list):
    num2 = 0
    if len(list) <= 2:
        print(f'primer valor: {list[0]}')
        num2 = list[1]
        return num2;
    else:
        print('Error, largo de la lista incorrecto valor max = 2')

print(imprimirVolver([0,1]))

#First Plus Length
def primeroMasLen(list):
    first= 0
    length = 0
    first = list[0]
    length= len(list)
    return first+length

print(primeroMasLen([1,2,3,4,5]))

#Valores mayores que el segundo
def mayorQueSegundo(list):
    newList=[]
    second=list[1]

    if len(list) > 2:
        for i in range(0,len(list),1):
            if (list[i]>second):
                newList.append(list[i])
    else:
        return False
    print('largo de mayores: ' + str(len(newList)))
    return newList

print(mayorQueSegundo([5,2,3,2,1,4]))

#Esta longitud, ese valor
def LongAndValue(size,value):
    newArr = []
    for i in range(0,size):
        newArr.append(value)
    return newArr
print(LongAndValue(4,7))

