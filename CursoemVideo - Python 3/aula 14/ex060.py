# //Faça um programa que lia um número qualquer e mostre o seu fatorial.
# //Ex: 5! = 5x4x3x2x1 = 120.
print('--' * 20)
print(' ' * 15 + 'MENU FATORIAL')
print('--' * 20)
n = int(input('Informe um número para calcular seu Fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
