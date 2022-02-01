# Crie um programa onde o usuário possa digitar vários 
# valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''                         VARIAVEIS GLOBAIS                      '''
print('=-=' * 15)
val_num = []
cont = 0
while True:
    n = int(input(' ' * 13 + 'Informe um valor: '))
    if n not in val_num:
        print('Valor adicionado com sucesso...')
        val_num.append(n)
    else:
        print('Esse número já está em nossa base de dados, tente outro.')
        print('=-=' * 15)
    '''                  VALIDAÇÃO DE STRING [S/N]                 '''
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'S':
        print('=-=' * 15)
    else:
        break
print('Fim programa...')
val_num.sort()
print(f'Os valores digitados foram: {val_num}')