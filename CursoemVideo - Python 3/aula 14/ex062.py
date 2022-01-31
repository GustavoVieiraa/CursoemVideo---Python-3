# //Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# //O programa encerrará quando ele disser que quer mostrar 0 termos.
print('-=-' * 15)
print(' ' * 15 + 'Gerador de PA')
print('-=-' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')