#Faça um programa que leia nome e peso de várias pessoas,                                      
#guardando tudo em uma lista. No final, mostre:
    #A) Quantas pessoas foram cadastradas.                          
    #B) Uma listagem com as pessoas mais pesadas.                                                                                                    
    #C) Uma listagem com as pessoas mais leves.
lista_chefe = list()
lista_dados = list()
maior = menor = 0
while True:
    lista_dados.append(str(input('Nome: ')))
    lista_dados.append(float(input('Peso[KG]: ')))
    if len(lista_chefe) == 0:
        maior = menor = lista_dados[1]
    else:
        if lista_dados[1] > maior:
            maior = lista_dados[1]
        if lista_dados[1] < menor:
            menor = lista_dados[1]
    lista_chefe.append(lista_dados[:])
    lista_dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N] ')).upper().strip()
    if resp == 'S':
        ('--' * 30)
    else:
        break
print('--' * 30)
print(f'Foram cadastradas {len(lista_chefe)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Dos seguintes: ', end='')
for verificacao in lista_chefe:
     if verificacao[1] == maior:
         print(verificacao[0], end='... ')
print()
print(f'O menor peso foi de {menor}Kg. Dos seguintes: ', end='')
for verificacao in lista_chefe:
    if verificacao[1] == menor:
        print(verificacao[0], end='... ')