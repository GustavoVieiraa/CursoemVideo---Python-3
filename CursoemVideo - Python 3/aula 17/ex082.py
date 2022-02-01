# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
print('--' * 30)
print(' ' * 13 + 'DIVIDINDO VALORES EM VÁRIAS LISTAS')
print('--' * 30)
lista_geral = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Informe um valor: '))
    if num%2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    lista_geral.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    if resp == 'S':
        print('--' * 30)
    if resp == 'N':
        break
print('--' * 30)
print(f'Sua lista com todos os valores: {lista_geral}')
print(f'Sua lista com os valores pares: {lista_pares}')
print(f'Sua lista com os valores impares: {lista_impares}')
