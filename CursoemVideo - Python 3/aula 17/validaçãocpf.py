'''                         VARIAVEIS GLOBAIS                      '''
num_cpf = []
print('=-=' * 25)
print(' ' * 30 + 'BANCO DE DADOS')
print('=-=' * 25)

while True:
    '''                         VALIDAÇÃO DE DADOS DENTRO DA LISTA                      '''
    cpf = int(input('|GOVERNO FEDERAL| CPF: '))
    if cpf not in num_cpf:
        num_cpf.append(cpf)
        print('|GOVERNO FEDERAL| CPF adicionado com sucesso!')
    else:
        print('Esse CPF já consta em nosso banco de dados.')
    '''                                VALIDAÇÃO DE CONTINUAÇÃO                         '''
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Gostaria de adicionar outro CPF? [S/N] ')).strip().upper()
    if resp == 'S':
        print('=-=' * 25)
    if resp == 'N':
        break
print('=-=' * 30)
'''                                INFORMAÇÕES GERAIS DA LISTA                           '''
print('|GOVERNO FEDERAL| Os CPFs armazenados foram: ')
for listagem in num_cpf:
        print(f'{listagem:^50}')
