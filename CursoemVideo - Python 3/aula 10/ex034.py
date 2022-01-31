# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('=====================CALCULO DE REAJUSTE SALARIAL - 2022=====================')
sal = float(input('INFORME SEU SALÁRIO: '))
if sal > 1250:
    print('REAJUSTE DE 10% | NOVO SALÁRIO: R${:.2f}'.format(((sal*10)/100) + sal))
else:
    print('REAJUSTE DE 15% | NOVO SALÁRIO: R${:.2f}'.format(((sal*15)/100) + sal))
print('=====================CALCULO DE REAJUSTE SALARIAL - 2022=====================')
