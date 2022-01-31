# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
num0 = 0
num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número outro: '))
num3 = int(input('Informe um número outro: '))
num4 = int(input('Informe um número outro: '))
valores = (num1, num2, num3, num4)
print(f'Os valores informados foram: {valores}')
print(f'O número 9 apareceu [{valores.count(9)}x]')
if num1 != 3 and num2 != 3 and num3 != 3 and num4 != 3:
    print('O valor 3 não apareceu em nenhuma posição.')
else:
    valores3 = (num0, num1, num2, num3, num4)
    print(f'O número 3 apareceu na {valores3.index(3)}º posição')
