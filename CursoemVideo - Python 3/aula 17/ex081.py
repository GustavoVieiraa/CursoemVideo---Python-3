#Crie um programa que vai ler vários números e colocar em uma lista.              
#Depois disso, mostre:
    #A) Quantos números foram digitados.
    #B) A lista de valores, ordenada de forma decrescente.   
    #C) Se o valor 5 foi digitado e está ou não na lista.'''
print('~~' * 27)
print(' ' * 13 + 'EXTRAINDO DADOS DE UMA LISTA')
print('~~' * 27)
lista = []
'''                         VALIDAÇÃO DE CONTINUAÇÃO                       '''
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'S':
            print('--' * 27)
    if resp == 'N':
        break
'''                         DESCRIÇÕES FINAIS                          '''
print('--' * 27)
print(f'Foram digitados {len(lista)}')
lista.sort(reverse=True)
print(f'Seus números digitados em sua lista em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 foi encontrado na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
