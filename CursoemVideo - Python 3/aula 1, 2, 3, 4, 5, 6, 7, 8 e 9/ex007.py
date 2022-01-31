# //Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = str(input('Qual é o seu nome: \n'))
print('Ok ', nome, ', vamos seguir com os calculos de média. \n')
N1 = float(input('Informe sua primeira nota: \n'))
N2 = float(input('Informe sua segunda nota: \n'))
M = (N1+N2)/2
print('A media entre a primeira nota: {:.1f} e a segunda nota:{:.1f}\n'.format(N1,N2))
print('é: {:.1f}\n'.format(M))
print('-' * 30)
