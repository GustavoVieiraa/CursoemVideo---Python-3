'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
print('--' * 15)
print(' ' * 10 + 'MEGA-SENA')
print('--' * 15)
lista = list()
jogos = list()
c = 0
contagem = 1
from random import randint
from time import sleep
num_jogos = int(input('|MEGA-SENA| Quantos jogos quer que sorteie? '))
while contagem <= num_jogos:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contagem += 1
print('=-=-=-=-=  ' + f'SORTEANDO {num_jogos} JOGOS' + '  =-=-=-=-=')
for i, nums in enumerate(jogos):
    print(f'Jogo {i+1}: {nums}')
    sleep(0.5)
print('=-=-=-=-=  ' + '<  BOA SORTE!!! >' + '  =-=-=-=-=')
