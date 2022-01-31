# //Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

print('--------------GAME OF ADIVINHAÇÃO V1.0-------------')
N = float(randint(0, 5))
print('COMPUTADOR JÁ ESCOLHEU UM Nº! ')
print('---------------------------------------------------')
SH = float(input('ESCOLHA O SEU Nº (0 a 5): '))
if SH == N:
    print('VOCÊ ADIVINHOU O Nº {:.0f}, PARABÉNS!'.format(N))
else:
    print('SEU NÚMERO FOI {:.0f}, E O DO COMPUTADOR {:.0f}, INFELIZMENTE VOCÊ PERDEU!'.format(SH, N))
print('----------------------END GAME----------------------')

