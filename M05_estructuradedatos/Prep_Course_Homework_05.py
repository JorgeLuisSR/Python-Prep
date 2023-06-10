#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

#ya que es una practic me reservo el derecho de usar paises
li = ["Argentina","Korea","Japón","China","Rusia","Alemania"]


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(li[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:


print(li[1:4])


# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(li))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(li[2:])

# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(li[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

li.append("Argentina")
li.append("India")

# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

li.insert(3,"Guatemala")

# 9) Concatenar otra lista a la ya creada

# In[22]:

#bueno... que tal continentes
fli = li+["Asia", "Africa", "Europa", "America", "Oceania"]

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:


print(fli[7])


# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

#Error index out of bounds en la mayoria de lenguajes

# 12) Eliminar un elemento de la lista

# In[25]:

fli.remove("Asia")

# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

#Error de elemento no encontrado

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

l=fli.pop()
print(l)

# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(fli*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

mi_tupla = tuple( x for x in range(1,21))
print(mi_tupla)

# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(mi_tupla[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in mi_tupla and 30 in mi_tupla)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

if not "París" in li:
    li.append("París")
    print("Paría was not in the first list, so i'd added it to the end")



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print("en la tupla aparece el numero 1 un total de "+ str(mi_tupla.count(1)) +" veces")
print("En la lista aparece el elemento Argentina un total de " + str(li.count("Argentina")) + " veces")

# 21) Convertir la tupla en una lista

# In[52]:

lista_de_tupla = list(mi_tupla)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

uno, dos, tres = mi_tupla[0:3]

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

mi_dict = dict()
for i in range(0, len(li)):
    mi_dict["Pais"+str(i)] = li[i]
print(mi_dict)




# 24) Imprimir las claves del diccionario

# In[59]:

print(mi_dict.keys)


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(mi_dict["Pais0"])
