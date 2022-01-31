# //Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
print('=-=' * 15)
print(15 * ' ' + '\033[33m MAIOR IDADE')
print('\033[0m=-=' * 15)
verif = int(input('VERIFICAR: '))
maior_id = 0
menor_id = 0
for c in range (1, verif + 1):
    id_pessoas = int(input('|{}|ANO DE NASCIMENTO: '.format(c)))
    if ano_atual - id_pessoas >= 18:
        maior_id = maior_id + 1
    elif ano_atual - id_pessoas < 18:
        menor_id = menor_id + 1
print('''         |Candidato(s) {} |
         |MAIOR DE IDADE {}|
         |MENOR DE IDADE {}|'''.format(verif, maior_id, menor_id))
print('=-=' * 15)
