# //Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# Se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('|==============|ALISTAMENTO MILITAR - 2022|==============|')
s = str(input('QUAL O SEU SEXO: [ M / F ]: '))
if s == 'M':
    ano_nasc = int(input('ANO DE NASCIMENTO: '))
    ano_atual = date.today().year
    if ano_nasc + 18 == ano_atual:
        print('DE ACORDO COM A SUA IDADE, ESTÁ NA HORA EXATA DE SE ALISTAR!')
    elif ano_nasc + 18 < ano_atual:
        print('DE ACORDO COM A SUA IDADE, VOCÊ PASSOU DO TEMPO DE ALISTAMENTO.')
        print('|ALISTAMENTO| VOCÊ DEVERIA TER SE ALISTADO EM: {}'.format(((ano_nasc + 18) + ano_atual) - ano_atual))
    elif ano_nasc + 18 > ano_atual:
        print('VOCÊ AINDA NÃO TEM IDADE PARA SE ALISTAR!')
        print('|ALISTAMENTO| VOCÊ DEVE SE ALISTAR EM: {}'.format(((ano_nasc + 18) - ano_atual) + ano_atual))
elif s == 'F':
    print("NO MOMENTO NÃO ESTAMOS ALISTANDO MULHERES.")
print('|==============|ALISTAMENTO MILITAR - 2022|==============|')
