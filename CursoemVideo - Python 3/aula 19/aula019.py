#Nessa aula, vamos aprender o que são DICIONÁRIOS e 
# como utilizar dicionários em Python. Os dicionários 
# são variáveis compostas que permitem armazenar vários 
# valores em uma mesma estrutura, acessíveis por chaves literais.
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
'''for k in pessoas.keys():
   #print(k)'''
'''for k in pessoas.values():
    print(k)'''
for k, v in pessoas.items():
    print(f'{k} = {v}')