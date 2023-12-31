# -*- coding: utf-8 -*-
"""Creando_estructuras-de-datos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H-CVARiSXaZeB72ggqkHpx464WEZMYTr

#PROBANDO INTRO
"""

datos = {'A': {'X': 1, 'Y': 3}, 'B': {'X': 2, 'Y': 4}}
df = pd.DataFrame(datos)
df

datos = [('A', 'B'), ('C', 'D')]
df = pd.DataFrame(datos, columns = ['L1', 'L2'],  index = ['C1', 'C2'])
df

df1 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df2 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
pd.concat([df1, df2])

datos = [[1, 2, 3], [4, 5, 6]]
index = 'X,Y'.split(',')
columns = list('ABC')[::1]
df = pd.DataFrame(datos, index, columns)
df

"""#CREANDO ESTRUCUTRAS"""

import pandas as pd

d = [2,3,4,5,6,0]

x = pd.Series(d)
x

a =["numero"+str(serie) for serie in range(6)]
a

x = pd.Series(data=d, index=a)
x

data = [2,4,6,8,10,12]

data ={"numero"+ str(i): i+1 for i in range(6)}
data

z = pd.Series(data)
z

x1 = x*10
x1

z1= x * z
z1

"""#**CREANDO DATAFRAMES**

DATAFRAME
"""

d =[[1,2,3],[4,5,6],[7,8,9]]
d

d1 = pd.DataFrame(d)
d1

ind = ["Linea" + str(i) for i in range(3)]
ind

d1 = pd.DataFrame(d, index =ind)
d1

col = ["Column" + str(i) for i in range(3)]
col
d1 = pd.DataFrame(d, index =ind, columns=col)
d1

"""DICCIONARY"""

a = {"Column0" : {"Linea0":1, "Linea1":4, "Linea2":7},
     "Column1" : {"Linea0":2, "Linea1":5, "Linea2":8},
     "Column2" : {"Linea0":3, "Linea1":6, "Linea2":9}}
a

d2 = pd.DataFrame(a)
d2

"""TUPLAS"""

n = [(1,2,3),(4,5,6),(7,8,9)]
n

d3 = pd.DataFrame(n)
d3

index = ["linea" + str(i) for i in range (3)]
index

columns = ["Column" + str(i) for i in range (3)]
columns

d3 = pd.DataFrame(n , index= index, columns=columns)
d3

"""CONVERTIR DATOS"""

d1[d1>0]="I"
d1

d2[d2>0]="E"
d2

d3[d3>0]="L"
d3

d4 = pd.concat([d1,d2,d3])
d4

d5 = pd.concat([d1,d2,d3], axis=1)
d5

numeros = [i for i in range(11)]
letras = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']

df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)

seleccion= df['N'].isin([i for i in range(11) if i % 2 == 0])
df = df[seleccion]
df

