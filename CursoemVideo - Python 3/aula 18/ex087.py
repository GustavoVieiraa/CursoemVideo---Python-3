'''Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.                       
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = soma = somalinhas = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c] 
    print()
for l in range(0, 3):
        somalinhas += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print('=-=' * 30)
print(f'A soma de todos os valores PARES da matriz foi de: {soma}')
print(f'A soma dos valores da terceira coluna é: {somalinhas}')
print(f'O maior valor da segunda linha é {maior}.')
print('=-=' * 30)
