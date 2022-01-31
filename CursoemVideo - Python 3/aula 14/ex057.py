# //Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# //Caso esteja errado, peça a digitação novamente até ter um valor correto.

# MINHA VERSÃO
'''print('=-=' * 20)
print(' ' * 20 + 'Validação de Genero')
print('=-=' * 20)
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('INFORME SEU GENERO: [M/F] ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Informação invalida, verifique e tente novamente!')
print('Obrigado pela informação, incluido no DataBase.')'''

# Versão Guanabara, ok!
print('=-=' * 20)
print(' ' * 20 + 'Validação de Genero')
print('=-=' * 20)
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrados. Banco de dados Salvo!'.format(sexo))
