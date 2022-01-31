# //Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print("-=-" * 15)
print("                RADAR ELETRONICO                 ")
vel = int(input('VELOCIDADE REGISTRADA: '))
multa = (vel*7) - (560)
if vel <= 80:
    print('Sua velocidade está dentro do limite.')
    print("-=-" * 15)
else: 
    print('Você excedeu a velocidade de 80KM. ')
    print('FOI MULTADO EM: R${}'.format(multa))

if vel > 80:
    pag = str(input('Você ira pagar essa multa? (S/N) '))
    if pag == 'S':
        print('Ok, iremos enviar no seu e-amail!')
        print("-=-" * 15)
    else: 
        print('Iremos te solicitar por correios.')
        print("-=-" * 15)
else:
    exit()

