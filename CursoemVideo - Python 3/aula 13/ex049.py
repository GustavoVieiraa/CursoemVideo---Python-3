# //Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('========---Tabuada v2.0---========')
n_tab = int(input('GOSTARIA DE VERIFICAR QUAL TABUADA?'))
print('========---Tabuada v2.0---========')
for c in range(0, 11):
    print('{} x {} = {}'.format(n_tab, c, n_tab*c))
print('========---Tabuada v2.0---========')
