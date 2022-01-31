#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No Final, mostre qual foi o maior e o menor valor digitado 
#e as suas respectivas posições na lista.
'''                   # Variaveis Globais                   '''
valores = []
maior = 0
menor = 0
'''                   # Back-end programa                    '''
print('-=-' * 15)
for cont in range(0, 5):
    valores.append(int(input(' ' * 13 + f'|Posição| {cont+1} |Informe um valor: ')))
    
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
'''                     # Layout do Menu                    '''
print('-=-' * 15)
print('  ' * 8 + '*-* MENU *-*')
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi: [{maior}] na(s) posição(s)  ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}... ', end='')
print()
print(f'O menor valor digitado foi: [{menor}] na(s) posição(s)  ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}... ', end='')
print()
print('-=-' * 15)
