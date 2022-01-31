# //Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
an = float(input('Informe um ângulo: \n'))
seno = sin(radians(an))
print('O ângulo {} tem o SENO de: {:.2f}.\n'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo {} tem o COSSENO de: {:.2f}.\n'.format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo {} tem a TANGENTE de: {:.2f}.\n'.format(an, tangente))
