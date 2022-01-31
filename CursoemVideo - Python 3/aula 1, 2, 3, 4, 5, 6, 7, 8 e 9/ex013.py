# //Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
SalAtual = int(input('Qual o seu salário: \n'))
SalAlt = (SalAtual * 15) / 100
SalNovo = (SalAtual + SalAlt)
print('Seu reajuste foi de 15%: {} \n'.format(SalAlt))
print('Seu novo salário é de: {} \n'.format(SalNovo))

