#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
from random import Random

li = [Random().choice(range(1,21)) for x in range(20)]
print(li)
def isPrime(n):
    if (n%2==0): return False
    if sum([int(x) for x in str(n)])%3==0: return False
    return True

print(str(li[0])+ " es primo? " + str(isPrime(li[0])))
# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def keepPrimes(n):
    return([x for x in n if isPrime(x)])

print(keepPrimes(li))
# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def mostRepeated(n, isMax=False):
    '''
    La funcion devuelve el elemento que más se repite en una lista
    sea el de menor o mayor valor de los que mas se repiten 
    '''
    re=list(n).copy()
    counter = 0
    ans = list()
    ans.append(re[0])
    for x in re:
        if re.count(x)>counter:
            ans = [x]
            counter = re.count(x)
        elif re.count(x) == counter and not x in ans:
            ans.append(x)
    if bool(isMax):
        return max(ans)
    else:
        return min(ans)
    
    
        
print(mostRepeated(li))
# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# In[45]:

print(mostRepeated(li, True))

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def unitChange(n, uo, ud):
    c=0
    if uo == 'F':
        c= (n-32) / (9/5)
    elif uo == 'K':
        c= n - 273.15
    elif uo == 'C':
        c=n
    else: return n

    if ud == 'C': return c
    elif ud == 'K': return c + 273.15
    elif ud == 'F': return c*(9/5) +32
    else: return n

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

temps=[0, 32, 273.15]
units = ['C', 'F', 'K']
res=list()
for x in units:
    for y in [z for z in units if z!=x]:
        for t in temps:
            res.append((t, x, y, unitChange(t, x, y)))

print(res)

# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factorial(n):
    if type(n)==type(float()) or n<1:
        print("Operacion no soportada")
        return 0
    elif n==1:
        return 1
    else: return n*factorial(n-1)

print(factorial(li[0]))