'''for c in range(0, 11):
    print(c)
print('FIM')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
print('FIM')'''

'''verific = ''
while verific != 'S':
    verific = str(input('GOSTARIA DE CONTINUAR??? [S/N] '))
print('Fim!')'''

'''resp = 'S'
while resp == 'S':
    num = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()
print('Fim!')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Informe um Nº: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você informou {} Nº pares e {} Nº impares'.format(par, impar))
