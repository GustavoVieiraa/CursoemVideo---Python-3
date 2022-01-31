# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from re import A


print('=-=-=-=-=-=-=-=-=ANALISADOR DE NÚMEROS=-=-=-=-=-=-=-=-=')
a = int(input('INFORME PRIMEIRO Nº: '))
b = int(input('INFORME SEGUNDO Nº: '))
c = int(input('INFORME TERCEIRO Nº: '))
# Verificando quem é o menor:
menor = a
if b<a and b<a:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
print('=-=-=-=-=-=-=-=-=ANALISADOR DE NÚMEROS=-=-=-=-=-=-=-=-=')