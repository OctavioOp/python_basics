# Tamaño grande
def bePositive(lst):
    newArr = []
    for i in range(0, len(lst)):
        if lst[i] > 0:
            newArr.append('Big')
        else:
            newArr.append(lst[i])
    return newArr


print(bePositive([-1, 3, 5, -5]))

# Contar positivos


def countPositives(lst):
    newArr = []
    count = 0
    for i in range(0, len(lst)):
        if lst[i] > 0:
            count += 1
            newArr.append(lst[i])
        else:
            newArr.append(lst[i])
    newArr.pop()
    newArr.append(count)
    return newArr


print(countPositives([-1, 1, 1, 1]))

# Suma total


def addEverything(lst):
    add = 0
    for i in range(0, len(lst)):
        add = add + lst[i]

    return add


print(addEverything([1, 2, 3, 4]))
print(addEverything([6, 3, -2]))

# Promedio


def average(lst):
    average = 0
    for i in range(0, len(lst)):
        average = average + lst[i]
    return average/len(lst)


print(average([1, 2, 3, 4]))

# Longitud


def length(lst):
    return len(lst)


print(length([37, 2, 1, -9]))

# minimo


def theSmallest(lst):
    aValue = lst[0]
    little = 0
    if len(lst) > 0:
        for i in range(0, len(lst)):
            if(aValue > lst[i]):
                little = lst[i]
    else:
        return False
    return little


print(theSmallest([37, 2, 1, -9]))

# Maximo


def theBiggest(lst):
    big = 0
    if len(lst) > 0:
        for i in range(0, len(lst)):
            if big < lst[i]:
                big = lst[i]

    else:
        return False
    return big


print(theBiggest([37, 2, 1, -9]))

# Análisis final


def ultimate_analisys(lst):
    suma = addEverything(lst)
    average1 = average(lst)
    little = theSmallest(lst)
    big = theBiggest(lst)
    length1 = length(lst)

    return {
        'total': suma,
        'promedio': average1,
        'minimo': little,
        'maximo': big,
        'longitud': length1
    }


print(ultimate_analisys([37, 2, 1, -9]))

# lista inversa


def invertedList(lst):
    newArr = []
    for i in range(len(lst)-1, -1, -1):
        newArr.append(lst[i])
    return newArr


print(invertedList([37, 2, 1,-9]))

'''factorial ejercicio extra'''
'''obtener todos los ceros a la derecha del factorial'''


def factorial(num):
    fact = 0
    for i in range(1, num + 1):
        fact = fact * i
    fact = str(fact)
    ceros = 0
    for j in range(len(fact)-1, 0, -1):
        if fact[j] == '0':
            ceros += 1
        else:
            break
    return ceros
