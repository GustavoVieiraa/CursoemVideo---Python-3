#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No Final, mostre qual foi o maior e o menor valor digitado 
#e as suas respectivas posições na lista.
'''                   # Variaveis Globais                   '''
valores = list()
maior = 0
menor = 10000000000000000
'''                   # Back-end programa                    '''
print('-=-' * 15)
for cont in range(0, 5):
    valores.append(int(input(' ' * 13 + f'|Posição| {cont} |Informe um valor: ')))
    cont +=1
for c, v in enumerate(valores):
    print(c, v)
    if v >= maior:
        maior = v
    if v <= menor:
        menor = v
'''                     # Layout do Menu                    '''
print('-=-' * 15)
print('  ' * 8 + '*-* MENU *-*')
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi: [{maior}] na posição {c}')
print(f'O menor valor digitado foi: [{menor}] na posição {c}')
print('-=-' * 15)
