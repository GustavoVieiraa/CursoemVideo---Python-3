# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# Se o usuário quer ou não continuar. No final, mostre:
# A> Quantas pessoas tem mais de 18 anos.
# B> Quantos homens foram cadastrados.
# C> Quantas mulheres tem menos de 20 anos.
from time import sleep
title = 'CADASTRE UMA PESSOA - 2022'
print('~~' * 25)
print(f'{title:^50}')
print('~~' * 25)
M = 0
F = 0
maioridade = 0
mul_menoridade = 0
# Estrutura para loop
while True:
    # Condição na idade
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    # Condição para escolha [M/F]
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        M += 1
    if sexo == 'F':
        F += 1
    if sexo == 'F' and idade < 20:
        mul_menoridade += 1
    # Condição para continuar [S]
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        sleep(1)
        print('Usuário cadastrado...')
        print('~~' * 15)
    # Condição para continuar [N]
    if continuar == 'N':
        print('~~' * 15)
        sleep(1.5)
        print('Finalizando cadastros...')
        sleep(1.5)
        break
print('--' * 20)
print(f'|REGISTROS| HOMENS CADASTRADOS: {M}')
print(f'|REGISTROS| MULHERES CADASTRADAS: {F}')
print(f'|REGISTROS| MULHERES COM MENOS DE 20 ANOS: {mul_menoridade}')
print(f'|REGISTROS| MAIORES DE IDADE: {maioridade}')
