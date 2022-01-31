# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequencia. No final, mostre uma listagem de preços organizando os dados em forma tabular.
title = 'LISTAGEM DE PREÇOS - 2022'
print('--' * 25)
print(f'{title:^52}')
print('--' * 25)
lista = ('Monitor', 1000, 'Mouse Razer', 250, 'Teclado Razer', 500, 'Gabinete Nox', 300, 'Celular A50', 1200,
'SSD Kingston', 200)
for cont in lista[0:1]:
    print(f'{cont}', end='............................R$   ')
for cont in lista[1:2]:
    print(f'{cont:.2f}')
for cont in lista[2:3]:
    print(f'{cont}', end='........................R$   ')
for cont in lista[3:4]:
    print(f'{cont:.2f}')
for cont in lista[4:5]:
    print(f'{cont}', end='......................R$   ')
for cont in lista[5:6]:
    print(f'{cont:.2f}')
for cont in lista[6:7]:
    print(f'{cont}', end='.......................R$   ')
for cont in lista[7:8]:
    print(f'{cont:.2f}')
for cont in lista[8:9]:
    print(f'{cont}', end='........................R$   ')
for cont in lista[9:10]:
    print(f'{cont:.2f}')
for cont in lista[10:11]:
    print(f'{cont}', end='.......................R$   ')
for cont in lista[11:12]:
    print(f'{cont:.2f}')
print('--' * 25)
