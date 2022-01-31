# //Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('===========|GAME BOX - PEDRA, PAPEL, TESOURA|===========')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
Escolha uma opção:
    _______________________
    |   [ 0 ] - PEDRA     |
    |   [ 1 ] - PAPEL     |
    |   [ 2 ] - TESOURA   |
    |_____________________|
''')
jogador = int(input('Qual é a sua jogada: '))
print('-=- ' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=- ' * 11)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
