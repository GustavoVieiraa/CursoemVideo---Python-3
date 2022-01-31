# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
title = 'CAIXA ELETRÔNICO - ITAU'
print('=-=' * 15)
print(f'{title:^45}')
print('=-=' * 15)
d50 = d20 = d10 = d1 = 0
while True:
    valor_sac = int(input('|CAIXA ELETRÔNICO| Valor: R$'))
    while valor_sac >= 50:
        valor_sac -= 50
        d50 += 1
    while valor_sac >= 20:
        valor_sac -= 20
        d20 += 1
    while valor_sac >= 10:
        valor_sac -= 10
        d10 += 1
    while valor_sac >= 1:
        valor_sac -= 1
        d1 += 1
    break
print(f'''----------------------------
|CAIXA ELETRÔNICO| NOTAS R$50: {d50}
|CAIXA ELETRÔNICO| NOTAS R$20: {d20}
|CAIXA ELETRÔNICO| NOTAS R$10: {d10}
|CAIXA ELETRÔNICO| NOTAS R$1: {d1}
|BANCO ITAU| Tenha um excelente dia.''')
