# //Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# //print('-' * 15)
# //nome = str(input('Nome da cidade: ')).strip()
# //print('Santo' in nome)
# //print('-' * 15)

print('------------PAINEL-------------')
cid = str(input('Nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
print('-------------------------------')
