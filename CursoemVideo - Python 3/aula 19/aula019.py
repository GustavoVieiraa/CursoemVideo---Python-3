#Nessa aula, vamos aprender o que são DICIONÁRIOS e 
# como utilizar dicionários em Python. Os dicionários 
# são variáveis compostas que permitem armazenar vários 
# valores em uma mesma estrutura, acessíveis por chaves literais.
'''dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
del dados['idade']'''
filme = {'titulo':'StarWars',
         'ano':1977,
         'diretor':'GeorgeLucas'}
# Para pegar os valores dos indices (keys)
print(filme.values())

# Para pegar as Keys ()
print(filme.keys())

# Para pegar todos os valores tanto os valores dos indices quanto os indices (keys):
print(filme.items())
print('=-=' '=-=')
for k, v in filme.items():
    print(f'O {k} é {v}')
