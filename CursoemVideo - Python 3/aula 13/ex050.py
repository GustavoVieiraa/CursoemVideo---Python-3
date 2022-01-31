# //Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
print('----------SYSTEM----------')
soma = 0
for cont in range(1, 7):
    num = int(input('LENDO {}º N°: '.format(cont)))
    if num%2 == 0:
        soma += num
print('A soma dos números pares foram: {}'.format(soma))
print('----------SYSTEM----------')
