# //Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('=-=' * 15)
print(' ' * 15 + 'QUEM É MAIS GORDO')
print('=-=' * 15)
men_peso = 0
mai_peso = 0
for c in range(1, 6):
    peso = float(input('|{}| PESO: '.format(c)))
    if peso == 1:
        mai_peso = peso
        men_peso = peso
    else:
        if peso > mai_peso:
            mai_peso = peso
        if peso < men_peso:
            men_peso = peso
print('O maior peso lido foi de {}Kg'.format(mai_peso))
print('O menor peso lido foi de {}Kg'.format(men_peso))
