# //Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
print('=-=' * 20 + 'CALCULADORA DE IMC' + '=-=' * 20)
kg = float(input('|CALCULADORA IMC| INFORME SEU PESO (Kg): '))
alt = float(input('|CALCULADORA IMC| INFORME SUA ALTURA (m): '))
imc = kg / (alt ** 2)
if imc < 18.5:
    print('============================CALCULADORA DE IMC============================')
    print('|CALCULADORA IMC| Seu peso: {:.1f}, Classificação = ABAIXO DO PESO.'.format(imc))
    print('============================CALCULADORA DE IMC============================')
elif imc > 18.6 and imc < 25:
    print('============================CALCULADORA DE IMC============================')
    print('|CALCULADORA IMC| Seu peso: {:.1f}, Classificação = PESO IDEAL.'.format(imc))
    print('============================CALCULADORA DE IMC============================')
elif imc > 25.1 and imc < 30:
    print('============================CALCULADORA DE IMC============================')
    print('|CALCULADORA IMC| Seu peso: {:.1f}, Classificação = SOBREPESO.'.format(imc))
    print('============================CALCULADORA DE IMC============================')
elif imc > 30.1 and imc < 40:
    print('============================CALCULADORA DE IMC============================')
    print('|CALCULADORA IMC| Seu peso: {:.1f}, Classificação = OBESIDADE.'.format(imc))
    print('============================CALCULADORA DE IMC============================')
elif imc > 40:
    print('============================CALCULADORA DE IMC============================')
    print('|CALCULADORA IMC| Seu peso: {:.1f}, Classificação = OBESIDADE MÓRBIDA.'.format(imc))
    print('============================CALCULADORA DE IMC============================')
else:
    print('Você informou algo errado, tente novamente.')
