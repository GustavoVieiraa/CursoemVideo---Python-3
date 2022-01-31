# // Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# // Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
title = 'Game Play - 2022'
print('~~' * 25)
print(f'{title:^50}')
print('~~' * 25)
c = 0
while True:
    # PARTE PC
    num_pc = randint(0, 10)
    esc_pc = ''
    # PARTE JOGADOR
    num_jogador = int(input('|JOGADOR| Digite um valor: '))
    esc_jogador = ' '
    while esc_jogador not in 'PpIi':
        esc_jogador = str(input('|JOGADOR| Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    # VARIAVEL GERAL
    tot = num_jogador + num_pc
    result = tot
    if result%2 == 0:
        result = str('|RESULTADO| PAR')
    else:
        result = str('|RESULTADO| IMPAR')
    # GANHADOR
    if esc_jogador == 'P':
        esc_pc = 'I'
    elif esc_jogador == 'I':
        esc_pc = 'P'
    ganhador = ''
    if esc_jogador == 'P' and result == str('|RESULTADO| PAR'):
        ganhador = 'GANHADOR É VOCÊ!'
        c += 1
    elif esc_jogador == 'I' and result == str('|RESULTADO| IMPAR'):
        ganhador = 'GANHADOR É VOCÊ!'
        c += 1
    elif esc_pc == 'P' and result == str('|RESULTADO| PAR'):
        ganhador = 'PC GANHOU!'
        break
    elif esc_pc == 'I' and result == str('|RESULTADO| IMPAR'):
        ganhador = 'PC GANHOU!'
        break
    print('PARRRRR')
    sleep(0.5)
    print('OUUUU')
    sleep(0.5)
    print('IMPAR')
    sleep(0.5)
    print(f'''
    ------------------------------------------------
    |MENU| JOGADOR JOGOU {num_jogador}
    |MENU| PC JOGOU {num_pc}
    |MENU| TOTAL {tot} e esse número é {result}.
    ------------------------------------------------
    ''')
    print(f'VOCÊ VENCEU! {c}x vezes.')
    print(f'|GANHADOR| {ganhador}')
# RESULTADO
print('PARRRRR')
sleep(0.5)
print('OUUUU')
sleep(0.5)
print('IMPAR')
sleep(0.5)
print(f'''
------------------------------------------------
|MENU| JOGADOR JOGOU {num_jogador}
|MENU| PC JOGOU {num_pc}
|MENU| TOTAL {tot} e esse número é {result}.
------------------------------------------------
''')
print('VOCÊ PERDEU!')
print(f'|GANHADOR| {ganhador}')
print(f'VOCÊ CONQUISTOU {c}x VITORIAS!')
