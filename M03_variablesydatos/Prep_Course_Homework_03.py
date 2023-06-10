#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

x = 1
print(x)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(x))



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Jorge"


# 5) Crear una variable que contenga un número complejo

# In[3]:

n_c = x+2j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(n_c))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

t="True"
tt=True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

# In[5]:

print(type(t))
print(type(tt))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

sum = 3 + 8.3



# 11) Realizar una operación de suma de números complejos

# In[2]:

ca = 2 +2j;cb = 4 - 1j
sumc = ca+cb


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
sumcr = ca + 4.6




# 13) Realizar una operación de multiplicación

# In[5]:


2*2


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

x = 27/4
print(x)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

y = 27//4
print (y)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
z = 27%4
print(z)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


print((4*y)+ z)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
a = "alfa"
b = "beto"
print(a+b)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print("2"==2)



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(int("2")==2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#"3,8" usa el simbolo ',' para separar la parte decimal de la parte entera del numero representado, mientras que en el ingles estandar se utiliza el simbolo '.'



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

x= 3
x-=1



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1<<2)

# El resultado aparece tras mover 2 bits "a la izquierda" del numero binario que representa el valor 1, es decir, pasar de 001 a 100
# El sistema de numeración binaria o binario es aquel que representa la cantidades numericas como un conjunto de valores de 2 estados, es decir que cada unidad representa uno de dos estados posibles
#   su combinación permite la representación de valores majores gracias al sistema de peso o valor según la posición del digito con repecto al numero completo, otra forma de calcularlo es representado cada unidad como en representación de una potencia de dos correspondiente a su posición




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print(2+"2")

# En Python a diferencia de otros lenguajes de programación, como javascript, el tipo de dato en cuestion determina si las operaciones aplicadas daran un resultado esperado o no, Python no permite las operaciones entre tipos de datos como texto y tipos numericos
# Por este motivo el convertir los valores al mismo tipo de dato (númerico o de cadena de texto) lograria resolver el error, concatenando a "22" o sumando 4



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

print(str(2) + "2")
print(2+int("2"))

