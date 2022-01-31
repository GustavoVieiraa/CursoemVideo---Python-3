# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-' * 15)
print(' ' * 15 + 'Gerador de PA')
print('-=-' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')