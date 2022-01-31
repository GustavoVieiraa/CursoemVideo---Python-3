# //Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

''' import math
CatOposto = float(input('Informe o comprimento do cateto oposto: \n'))
CatAdjacente = float(input('Informe o comprimento do cateto adjacente: \n'))
CatOposto = (CatOposto**2)
CatAdjacente = (CatAdjacente**2)
H = (CatAdjacente + CatOposto)
H = H**(1/2)
print('Sua Hipotenusa é: {:.2f}'.format(H))'''

'''co = float(input('Qual o cateto oposto: '))
ca = float(input('Qual o cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A sua hipotenusa é: {:.2f}'.format(h))'''

