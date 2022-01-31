# //Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
print('= ' * 30)
print(' ' * 20 + 'Analisador Completo')
print('= ' * 30)
quant_vezes = int(input('VERIFICAR: '))
idade_media = 0
nomevelho = ''
homem_mais_velho = 0
for pessoa in range (0, quant_vezes):
    nome = str(input('NOME: ')).strip
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: ')).strip
    print('=' * 10)
    idade_media += idade
    if pessoa == 1 and sexo == "M":
        homem_mais_velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nomevelho = nome
idade_media = (idade_media/quant_vezes)
print('A média das {} idades é de {:.0f} anos.'.format(quant_vezes, idade_media))
print('O homem mais velho tem {} anos e se chama {}'.format(homem_mais_velho, nomevelho))
