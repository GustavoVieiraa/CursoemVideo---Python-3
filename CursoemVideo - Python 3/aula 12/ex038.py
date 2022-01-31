 #// Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

 #// – O primeiro valor é maior

 # // – O segundo valor é maior

 # // – Não existe valor maior, os dois são iguais
print('============LEITOR DE NÚMEROS============')
n1 = int(input('INFORME PRIMEIRO Nº INTEIRO: '))
n2 = int(input('INFORME SEGUNDO Nº INTEIRO: '))
if n1 > n2:
    print('Primeiro valor ({}) é maior que o Segundo valor ({})'.format(n1, n2))
elif n2 > n1:
    print('Segundo valor ({}) é maior que o Primeiro valor ({})'.format(n2, n1))
else:
    print('Primeiro ({}) e Segundo ({}) valores são iguais!'.format(n1, n2))
print('============LEITOR DE NÚMEROS============')
