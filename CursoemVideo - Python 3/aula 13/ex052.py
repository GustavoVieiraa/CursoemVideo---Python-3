# //Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('\033[30m=-=' * 15)
print(15 * " " + '\033[m Número Primo')
print('\033[30m=-=' * 15)
num = int(input('\n\033[m DIGITE UM NÚMERO: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!!')
else:
    print('E por isso ele NÃO É PRIMO!')