# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequencia. No final, mostre uma listagem de preços organizando os dados em forma tabular.
title = 'LISTAGEM DE PREÇOS - 2022'
print('--' * 25)
print(f'{title:^52}')
print('--' * 25)
lista = ('Monitor', 1000, 'Mouse Razer', 250, 'Teclado Razer', 500, 'Gabinete Nox', 300, 'Celular A50', 1200,
'SSD Kingston', 200, 'Fonte 450W', 150, 'Fone Redmi', 100, 'Memoria DDR4 8GB', 250)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30} R$', end='  ')
    if pos % 2 == 1:
        print(f'{lista[pos]:.2f}')
print('--' * 25)
