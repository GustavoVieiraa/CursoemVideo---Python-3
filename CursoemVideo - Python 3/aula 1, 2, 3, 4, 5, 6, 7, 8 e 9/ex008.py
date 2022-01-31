# //escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# //M = float(input('Informe os Metros: \n'))
# //print('Esse valor em metros ({}), convertido em centímetros será: '.format(M), M*100)
# //print('Esse valor em metros ({}), convertido em milímetros, será: '.format(M), M*1000)

medidas = float(input('Informe uma distância em metros: \n'))
dm = medidas * 10
cm = medidas * 100
mm = medidas * 1000
dam = medidas / 10
hm = medidas / 100
km = medidas / 1000
print('Essa distância em M({}), corresponde à {}dm | {:.0f}cm | {:.0f}mm.\n'.format(medidas, dm, cm, mm))
print('-' * 50)
print('\nEssa distância em M({}), corresponde à {}dam | {}hm | {}km.'.format(medidas, dam, hm, km))
