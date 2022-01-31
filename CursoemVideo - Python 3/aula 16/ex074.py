# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# Valor que estão na tupla.
# Minha resolução, funcionou!
'''from random import randint
title = 'Gerador de números em Tupla'
print('~~' * 25)
print(f'{title:^55}')
print('~~' * 25)
menor = 10
maior = 0
# Sorteador de números 
print('Os valores sorteados foram: ')
for c in range (0, 5):
c += 1
valores = randint(0, 10)
if valores > maior:
maior = valores
if valores < menor:
menor = valores
print(valores, end=' ')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''


from random import randint
title = 'Gerador de números em Tupla'
print('~~' * 25)
print(f'{title:^55}')
print('~~' * 25)
num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Os números sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')