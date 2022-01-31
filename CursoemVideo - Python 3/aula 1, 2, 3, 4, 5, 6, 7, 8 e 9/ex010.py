# //Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# //Considerando -> US$1,00 = R$3,27.
C = float(input('Quantos reais você tem na Carteira: \n'))
Dolar = (C / 3.27)
print('Com {} em Reais, você consegue comprar US${:.2f}'.format(C, Dolar))
