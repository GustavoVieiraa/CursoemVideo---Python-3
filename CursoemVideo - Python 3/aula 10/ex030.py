# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
print("-=-" * 16)
print('-------------------SYSTEM OPEN-------------------')
n = float(input('INFORME UM Nº: '))
if (n%2) == 1:
    print('{:.0f} é IMPAR!'.format(n))
else:
    print('{:.0f} é PAR!'.format(n))
print('------------------SYSTEM CLOSE--------------------')