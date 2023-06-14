#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        
    def acelerar(self):
        print ("driving as a good", self.tipo)
    def frenar(self):
        print ("stoping the movement of my", self.color, "painting")
    def doblar(self):
        print("turning around with", self.cilindrada, "power")


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

#done

import sys
if not sys.path.__contains__(r"C:/xampp/htdocs/Python-Prep"):
    sys.path.append(r"C:/xampp/htdocs/Python-Prep")
    print(sys.path)


# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

moto = Vehiculo("blue", "truck", 1000)
auto = Vehiculo("puple", "air-plane", 5000)
tractor = Vehiculo("red", "tractor", 200)

moto.acelerar()
auto.doblar()
tractor.frenar()

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class Vehiculo:
    direcciones  =  ["North", "East", "South", "West"]
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.speed = 0
        self.direction = 0 # North
        
    def acelerar(self):
        print ("speeding as a good", self.tipo)
        self.speed+= self.cilindrada/20
    def frenar(self):
        print ("stoping the movement of my", self.color, "painting")
        self.speed-=self.cilindrada/10
        if self.speed<0 : self.speed=0
    def doblar(self, direction = True):
        '''gira el vehiculo hacia la dereche [True] o hacia la izquierda [False], default hacia la derecha'''
        print("turning around with", self.cilindrada, "power")
        if bool(direction): self.direction=(self.direction+1)%4
        else: self.direction = self.direction=4+(self.direction-1)%4
    def getInfo(self):
        print(f"The vehicle is a {self.tipo}, has a {self.color} color and works with a {self.cilindrada} engine displacement")
    def getState(self):
        print(f"The vehicle has an absurd speed of {self.speed}m/h, also, is going to the {self.direcciones[self.direction]}")



# In[13]:


tractor = Vehiculo("red", "tractor", 200)
tractor.acelerar()
tractor.acelerar()
tractor.acelerar()
tractor.doblar()
tractor.doblar()
tractor.doblar()
tractor.frenar()
tractor.frenar()
tractor.frenar()
tractor.getInfo()
tractor.getState()
tractor.doblar()
tractor.acelerar()
tractor.getState()




# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
import M07_funciones.Prep_Course_Homework_07 as m7

class WeirdCalc:
    def __init__(self):
        print("WeirdCalculator has begun its program :)")
    def isPrime(self, n):
        return m7.isPrime(n)
    def factorial(self, n):
        return m7.factorial(n)
    def unitChange(self, n, uo, ud):
        return m7.unitChange(n, uo, ud)
    def mostRepeated(self, n, isMax=False):
        return m7.mostRepeated(n, isMax)
    def keepPrime(self, n):
        return m7.keepPrimes(n)


# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
wc = WeirdCalc()

print(f"es primo el 7? {wc.isPrime(7)}")
print(f"Factorial de 10: {wc.factorial(10)}")
print(f"-1 grados son {wc.unitChange(-1, 'C', 'F')} farenheitz")
print(f"El número mas repetido de la lista {[1,1,1,2,2,2,3,3,3,3,3,4,5,5,5,5,5]} (seleccionando el más pequeño si hay más de uno) es {wc.mostRepeated([1,1,1,2,2,2,3,3,3,3,3,4,5,5,5,5,5])}")
print(f"De la lista {list(range(1,21))} los unicos primos son {wc.keepPrime(list(range(1,21)))}")


# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

class WeirdCalc:
    def __init__(self, lista):
        print("WeirdCalculator has begun its program :)")
        self.li = lista
    def isPrime(self, n):
        return m7.isPrime(n)
    def factorial(self, n):
        return m7.factorial(n)
    def unitChange(self, n, uo, ud):
        return m7.unitChange(n, uo, ud)
    def mostRepeated(self, isMax=False):
        return m7.mostRepeated(self.li, isMax)
    def keepPrime(self):
        return m7.keepPrimes(self.li)




# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:


import modulaso

c = modulaso.Calc(list(range(1,10)) + list(range(2,7)) + list(range(4,6)))

print(f"es primo el 7? {c.isPrime(7)}")
print(f"Factorial de 10: {c.factorial(10)}")
print(f"-1 grados son {c.unitChange(-1, 'C', 'F')} farenheitz")
print(f"El número mas repetido de la lista (seleccionando el más pequeño si hay más de uno) es {c.mostRepeated()}")
print(f"De la lista los unicos primos son {c.keepPrime()}")


# %%
