# //Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido.

from random import choice
n1 = str(input('Informe 1º Aluno: \n'))
n2 = str(input('Informe 2º Aluno: \n'))
n3 = str(input('Informe 3º Aluno: \n'))
n4 = str(input('Informe 4º Aluno: \n'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

