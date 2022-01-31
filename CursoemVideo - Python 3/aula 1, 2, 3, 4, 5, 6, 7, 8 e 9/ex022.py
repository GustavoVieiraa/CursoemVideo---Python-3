# //Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as Letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todoo (sem considerar espaços)
# Quantas letras tem o primeiro nome.
nome = str(input('Qual o seu nome completo: \n')).strip()
print('-' * 15, 'PAINEL DE APRESENTAÇÃO', '-' * 20)
print('O nome todo em maiúsculo:', nome.upper())
print('O nome todo em minúsculo:', nome.lower())
print('Seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))
# // print('Todos os caracteres sem considerar os espaços:',len(nome.replace(' ', '')))
dividido = nome.split()
print('Seu Primeiro nome tem: {} letras'.format(len(dividido[0])))
print('-' * 15, 'FIM PAINEL DE APRESENTAÇÃO', '-' * 15)
