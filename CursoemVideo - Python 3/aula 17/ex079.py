# Crie um programa onde o usuário possa digitar vários 
# valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''                         VARIAVEIS GLOBAIS                      '''
print('=-=' * 15)
val_num = []
while True:
    n = int(input(' ' * 13 + 'Informe um valor: '))
    if n not in val_num:
        print(' ' * 8 + '~~' * 15)
        print(' ' * 8 + 'Valor adicionado com sucesso...')
        print(' ' * 8 + '~~' * 15)
        val_num.append(n)
    else:
        print('Esse número já está em nossa base de dados, tente outro.')
        print('=-=' * 15)
    '''                  VALIDAÇÃO DE STRING [S/N]                 '''
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input(' ' * 11 + 'Quer continuar? [S/N] ')).strip().upper()
    if resp == 'S':
        print('=-=' * 15)
    elif resp == 'N':
        break
print('=-=' * 15)
val_num.sort()
print(' ' * 7 + f'Os valores digitados foram: {val_num}')
print('=-=' * 15)
