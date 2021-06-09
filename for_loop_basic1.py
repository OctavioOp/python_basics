# imprime de 0 a 150
from typing import cast


for x in range(0, 151):
    print(x)

# Multiples de 5
for m in range(5, 1001, 5):
    print(m)


# Contar, Dojo Way
for i in range(1, 101):
    if (i % 5 == 0) and (i % 2 != 0):
        print('Coding')

    elif (i % 10 == 0) and (i % 2 == 0):
        print('Coding Dojo')


# ¡Uf, Eso es bastante grande!
sum = 0
for s in range(0, 500001, 1):
    if s % 2 != 0:
        sum = sum + s
print(sum)

# Cuenta regresiva por cuatro
for c in range(2018, 0, -4):
    print(c)

# Contador flexible
lowNum = 2
highNum = 9
mult = 3

for f in range(lowNum, highNum+1):
    if f % mult == 0:
        print(f)


# numeros primos
arr = []
for p in range(0, 1000):
    if p == 1:
        continue
    elif p == 2:
        arr.append(p)
        arr.append(3)
        arr.append(5)
        arr.append(7)
        arr.append(11)
    elif p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0 and p % 11 != 0:
        arr.append(p)
print(arr)

def primo(num):
    for t in range (2,num):
        if num%t==0:
            return False
    return True

primos100 = [x for x in range(2,1001) if primo(x) is True]
print (primos100)