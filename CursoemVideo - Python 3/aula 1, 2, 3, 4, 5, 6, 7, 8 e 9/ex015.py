# //Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias alugou o carro: \n'))
km = float(input('Quantos KMs você rodou com o carro: \n'))
pago = (dias * 60) + (km * 0.15)
print('{:.0f} dias e {}kms rodados, o total a pagar é: R${:.2f}'.format(dias, km, pago))
