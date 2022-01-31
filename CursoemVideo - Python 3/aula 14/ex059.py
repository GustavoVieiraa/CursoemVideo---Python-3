# // Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
from time import sleep
print('==' *25)
print(' ' * 20 + '|MENU - v2.0|')
print('==' * 25)
maior = 0
m = 0
num1 = int(input('INFORME PRIMEIRO Nº: '))
num2 = int(input('INFORME SEGUNDO Nº: '))
while m != 5:
    m = int(input('''
        Gostaria de:
        [1]SOMAR
        [2]MULTIPLICAR
        [3]MAIOR
        [4]NOVOS NÚMEROS
        [5]SAIR DO PROGRAMA
    '''))
    if m == 1:
        print('==' * 15)
        print('|SOMA| A soma de {} e {} é {}'.format(num1, num2, (num1 + num2)))
        print('==' * 15)
    elif m == 2:
        print('==' * 22)
        print('|MULTIPLICAÇÃO| O resultado de {} x {} é {}'.format(num1, num2, (num1 * num2)))
        print('==' * 22)
    elif m == 3:
        print('==' * 15)
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('|MAIOR Nº| Entre {} e {} o maior número é {}'.format(num1, num2, maior))
        print('==' * 15)
    elif m == 4:
        num1 = int(input('INFORME PRIMEIRO Nº: '))
        num2 = int(input('INFORME SEGUNDO Nº: '))
    elif m == 5:
        print(' ')
    else:
        print('Opção invalida, tente novamente.')
print('Finalizando...')
sleep(2.5)
print('==' *25)
print(' ' * 20 + 'FIM | MENU - v2.0')
print('==' * 25)
