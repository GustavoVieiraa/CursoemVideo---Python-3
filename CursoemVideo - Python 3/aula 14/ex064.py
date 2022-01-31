# //Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('~~' * 20)
print(' ' * 10 + 'TUDO!!! - 999')
print('~~' * 20)
n = c = s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar o Software]: '))
    if n != 999:
        c = c + 1
        s += n
    else:
        s += n - 999
print('Você digitou {} Nº e a soma entre eles foi {}.'.format(c, s))
