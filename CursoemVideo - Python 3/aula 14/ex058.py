# //Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# //Só que agora o jogador vai tentar adivinhar até acertar,
# //mostrando no final quantos palpites foram necessários para vencer.
from random import randint
num_computador = randint(0, 10)
print('=-=' * 20)
print(' ' * 23 + 'SORTE OU AZAR?')
print('=-=' * 20)
num_jogador = 11
cont_tentativas = 0
while num_jogador != num_computador:
    num_jogador = int(input('JOGUE: '))
    if num_jogador != num_computador:
        cont_tentativas += 1
        print('Você errou, tente novamente. ')
        if num_jogador < num_computador:
            print('Mais... você consegue!')
        if num_jogador > num_computador:
            print('Menos... você consegue!')
print('''PARABÉNS, VOCÊ VENCEU!
        |COMPUTADOR| {}
        |  JOGADOR | {}
        |TENTATIVAS| {}'''.format(num_computador, num_jogador, cont_tentativas))
    