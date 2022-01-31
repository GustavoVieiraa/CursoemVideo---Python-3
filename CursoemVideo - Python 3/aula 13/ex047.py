# //Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
print('=-= ' * 15 + 'CONTAGEM DE PARES' + '=-= ' * 15)
num = int(input('Nº PARES ATÉ: '))
for c in range(0, num+2, 2):
    sleep(0.2)
    print('Nº PAR: {}'.format(c))
print('=-= ' * 15 + 'CONTAGEM DE PARES' + '=-= ' * 15)
