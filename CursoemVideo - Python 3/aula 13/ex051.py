# //Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
print('=-=' * 15)
print(' ' * 15 + 'TERMOS DE UMA PA')
print('=-=' * 15)
pri_term = int(input('INFORME 1º TERMO: '))
r = int(input('RAZÃO: '))
dec = pri_term + (10 - 1) * r
for c in range(pri_term, dec + r, r):
    print('{}... '.format(c))
