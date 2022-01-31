# // Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# // ''' from math import floor
# // num = float(input('Digite um Nº quebrado: '))
# //print('Seu número {} foi concertado {}'.format(num, floor(num))) '''

from math import trunc
num = float(input('Digite um Nº: '))
print('Seu número é {}, e sua porção inteira é {}.'.format(num, trunc(num)))
