# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
from time import sleep

title = '₢MENU₢'
print('~~' * 20)
print(f'{title:^40}')
print('~~' * 20)
num = s = cont = 0
while True:
    num = int(input('''    
    Obs: Para STOP digite (999).
    INFORME UM NÚMERO: '''))
    if num == 999:
        print('Finalizando programa...')
        sleep(1.5)
        print('Totalizando números...')
        sleep(2)
        print('Fazendo soma entre os números...')
        sleep(2.5)
        break
    cont += 1
    s += num
print(f'Foram digitados {cont} números e a soma entre eles foi de {s}.')
