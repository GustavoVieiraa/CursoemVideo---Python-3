# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A> Qual é o total gasto na compra.
# B> Quantos produtos custam mais de R$1000,00
# C> Qual é o nome do produto mais barato.
title = 'Estátisticas - 2022'
print('~~' * 20) 
print(f'{title:^40}')
print('~~' * 20)
# Variavel Global
value_product = tot_gasto = product_1000 = cont = small_product = 0
name_product = add_product = small_product_name = ''
while True:
    # Entrada de Nome e valor do Produto
    name_product = str(input('|WALMART| NOME PRODUTO: ')).upper().strip()
    value_product = float(input('|WALMART| VALOR PRODUTO: R$ '))
    cont += 1
    # Condição se deseja continuar ou não
    add_product = ' '
    while add_product not in 'SsNn':
        add_product = str(input('|WALMART| ADICIONAR PRODUTO? [S/N] ')).upper().strip()[0]
    # Condição para continuar o programa
    if add_product == 'S': 
        print('~~' * 15)
        # Soma de valores
        tot_gasto += value_product
        # Valores maiores que 1000
        if value_product >= 1000:
            product_1000 += 1
        if cont == 1:
            small_product = value_product
            small_product_name = name_product
        else:
            if value_product < small_product:
                small_product = value_product
                small_product_name = name_product
    # Condição para não continuar o programa
    elif add_product == 'N':
        print('~~' * 15)
        # Soma de valores
        tot_gasto += value_product
        # Valores maiores que 1000
        if value_product >= 1000:
            product_1000 += 1
        if cont == 1:
            small_product = value_product
        else:
            if value_product < small_product:
                small_product = value_product
        break
print(f'|WALMART - CAIXA| R${tot_gasto:.2f}')
print(f'|WALMART - CAIXA| Produtos acima de R$1000,00 [{product_1000}]')
print(f'|WALMART - CAIXA| O produto mais barato foi {small_product_name} e custou R${small_product:.2f}')
