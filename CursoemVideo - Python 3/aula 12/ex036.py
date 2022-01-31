# // Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('======================|CONSULTA EMPRESTIMO - 2022|======================')
val_casa = float(input('|BANCO INTER| VALOR DA CASA:'))
salario = float(input('|BANCO INTER| SEU SALÁRIO: '))
anos_emp = int(input('|BANCO INTER| FINANCIAR EM QUANTOS ANOS: '))
prest_mensal = (val_casa/(anos_emp*12))
salario_trinta = ((salario * 30) / 100)
if salario > prest_mensal:
    print("=============================")
    print('=====EMPRESTIMO APROVADO=====')
    print('=============================')
    print('30% do seu Salário é: R${:.2f}'.format(salario_trinta))
    print('E a parcela ficou em R${:.2f}'.format(prest_mensal))
    print('=============================')
else:
    print('==============================')
    print('=====EMPRESTIMO REPROVADO=====')
    print('==============================')
    print('30% do seu Salário é: R${:.2f}'.format(salario_trinta))
    print('E a parcela ficou em R${:.2f}'.format(prest_mensal))
    print('=============================')
