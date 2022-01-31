# //Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# //mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# //O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('~~' * 15)
print(' ' * 10 + 'MENU v2.0.0')
print('~~' * 15)
condicao = 'S'
quant = s = m = maior = menor = 0
while condicao in 'Ss':
    num = int(input('|MENU| informe um número: '))
    quant += 1
    s += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    condicao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = (s/quant)
print('''-----------------==MENU==-----------------
|QUANT DE NÚMEROS INFORMADOS| {}
|MÉDIA| {}
|MAIOR NÚMERO| {}
|MENOR NÚMERO| {}
'''.format(quant, m, maior, menor))
