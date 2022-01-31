# //Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5 de desconto.
Val = float(input('Qual o valor do produto: R$ \n'))
DescontVal = (Val * 5) / 100
ValFinal = (Val - DescontVal)
print('O valor do desconto é de: R${:.2f} \n'.format(DescontVal))
print('O valor final do produto é: R${:.2f} \n'.format(ValFinal))
