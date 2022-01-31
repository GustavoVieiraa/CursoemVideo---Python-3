# //Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('------------------SYSTEM CCAR------------------')
km = float(input('DISTANCIA PERCORRIDA (KM): '))
if km <= 200:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('VALOR A SER PAGO: R${:.2f}'.format(km*0.5))
    print('DISTANCIA PERCORRIDA: {:.0f}KM'.format(km))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
else:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('VALOR A SER PAGO: R${:.2f}'.format(km*0.45))
    print('DISTANCIA PERCORRIDA: {:.0f}KM'.format(km))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('------------------SYSTEM CCAR------------------')
