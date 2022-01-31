# // Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será 
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('==============CONVERSOR DE NÚMEROS==============')
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('Nº {} convertido para BINÁRIO é igual a: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('Nº {} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('Nº {} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO ESCOLHIDA INVALIDA!')
print('==============CONVERSOR DE NÚMEROS==============')
