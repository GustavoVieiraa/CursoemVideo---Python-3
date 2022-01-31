# // Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('----------PAINEL BY X:II----------')
F = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A", aparece: {}'.format(F.count('A')))
print('A primeira vez que a letra A aparece é na posição {}'.format(F.find('A')+1))
print('A ultima vez que a letra A aparece é na posição {}'.format(F.rfind('A')+1))
