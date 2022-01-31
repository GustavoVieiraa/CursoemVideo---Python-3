# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
title = 'Tabuada v3.0'
print('~' * 30)
print(f'{title:^30}')
print('~' * 30)
# VARIAVEIS GLOBAIS
while True:
    num_tabuada = int(input('|Menu| Qual tabuada? : '))
    if num_tabuada < 0:
        break
    c = 0
    print('-' * 25)
    while c < 10:
        c += 1
        result = (num_tabuada * c)
        print(f'{num_tabuada} x {c} = {result}')
print('Suas verificações finalizaram, VOLTE SEMPRE!')
