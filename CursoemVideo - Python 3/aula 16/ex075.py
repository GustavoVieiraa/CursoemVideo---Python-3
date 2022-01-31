# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
num0 = 0
num = (int(input('Informe um número: ')),
        int(input('Informe outro número: ')),
        int(input('Informe mais um número: ')),
        int(input('Informe o último número: ')))
valores = (num)
print(f'Você digitou os valores {num}')
print(f'Você digitou {num.count(9)}x o número [9].')
if 3 in num:
    print(f'O número três apareceu na {num.index(3)+1}ª posição')
else:
    print('O número três não apareceu em nenhuma posição.')
print('Os valores pares são: ', end=' ')
for n in num:
    if n%2 == 0:
        print(n, end=' ')
