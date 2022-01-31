# //O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Informe nome: '))
n2 = str(input('Informe nome: '))
n3 = str(input('Informe nome: '))
n4 = str(input('Informe nome: '))
apresentacao = [n1, n2, n3, n4]
# //Comando para embaralhar / ou sortear aleátorio com ordem!
shuffle(apresentacao)
print('A ordem de apresentação dos trabalhos será: {}'.format(apresentacao))




