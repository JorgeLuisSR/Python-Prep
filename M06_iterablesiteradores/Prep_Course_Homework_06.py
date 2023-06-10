#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:


li = list()
i=-15
while i < 0:
    li.append(i);i+=1


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
i=0
while i < len(li):
    if li[i]%2 == 0:
        print(li[i]) 
    i+=1
        

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for x in li:
    if x%2==0:
        print(x)

# 4) Utilizar el iterable para recorrer sólo los prime ros 3 elementos

# In[7]:

print(li[0:3])

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for x in enumerate(li):
    print(x)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1,2,5,7,8,10,13,14,15,17,20]
for x in range(1,21):
    if not x in lista:
        lista.insert(x-1,x)
print(lista)
# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

fibonachi = [0,1]
for x in range(2,31):
    fibonachi.append(fibonachi[x-1]+fibonachi[x-2])
print(fibonachi)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(fibonachi))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

for i in range(len(fibonachi)-1,len(fibonachi)-6,-1):
    print(fibonachi[i-1]/fibonachi[i])


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i in range(len(cadena)):
    if cadena[i] == 'n': print("encontrado en el caracter n° "+str(i+1))


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

dictionary = dict()
for x in range(10):
    dictionary[cadena[:x+1]] = sorted(cadena[:x+1])
for x in dictionary:
    print(x)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

listac = list(cadena)
print(x for x in listac)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

zipped_list = zip(li, listac)

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis1 = [x for x in lis if x%7==0]

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
count = 0
for i in range(len(lis)):
    if not type(lis[i]) == type(list()):
        count+=1
        continue
    count+=len(lis[i])

print(count)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

selec = [x for x in lis if type(x)!= type(list())]
print(selec)


# %%
