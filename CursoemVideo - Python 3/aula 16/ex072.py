# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numbers = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
title = 'CONVERSOR de NÚMEROS - 2022'
print('~~' * 25)
print(f'{title:^50}')
print('~~' * 25)
while True:
    num = int(input('|CONVERSOR| Informe um N°: '))
    if num >= 0 and num <= 20:
        print('--' * 8)
        print(f'{numbers[num]:^15}')
        print('--' * 8)
    elif num == 999:
        break
    else:
        print('informação invalida, tente novamente.')
print('Fim programa.')