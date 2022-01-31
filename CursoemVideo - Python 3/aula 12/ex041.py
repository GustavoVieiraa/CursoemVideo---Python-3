# //A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
print('=-=' * 15 + 'CLASSIFICAÇÃO DE ATLETAS' + '=-=' * 15)
ano_nasc = int(input('ANO NASCIMENTO: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    print('=============================CLASSIFICAÇÃO=============================')
    print('|CLASSIFICAÇÃO| Com {} anos, você está na categoria MIRIM.'.format(idade))
    print('=============================CLASSIFICAÇÃO=============================')
elif idade >= 10 and idade <=14:
    print('=============================CLASSIFICAÇÃO=============================')
    print('|CLASSIFICAÇÃO| Com {} anos, você está na categoria INFANTIL.'.format(idade))
    print('=============================CLASSIFICAÇÃO=============================')
elif idade >=15 and idade <=19:
    print('=============================CLASSIFICAÇÃO=============================')
    print('|CLASSIFICAÇÃO| Com {} anos, você está na categoria JÚNIOR.'.format(idade))
    print('=============================CLASSIFICAÇÃO=============================')
elif idade >=19 and idade <=25:
    print('=============================CLASSIFICAÇÃO=============================')
    print('|CLASSIFICAÇÃO| Com {} anos, você está na categoria SÊNIOR.'.format(idade))
    print('=============================CLASSIFICAÇÃO=============================')
elif idade >=25:
    print('=============================CLASSIFICAÇÃO=============================')
    print('|CLASSIFICAÇÃO| Com {} anos, você está na categoria MASTER.'.format(idade))
    print('=============================CLASSIFICAÇÃO=============================')
else:
    print('VOCÊ É RETARDADO, NÃO SABE PREENCHER NEM QUANDO NASCEU. Tente novamente.')
