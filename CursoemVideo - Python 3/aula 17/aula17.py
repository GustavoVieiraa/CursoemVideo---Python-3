# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
# acessíveis por chaves individuais.
'''#Para adicionar um item em uma lista temos o comando .append()
#ex. lanche.append('biscoito')

#Para adicionar um item em qualquer lugar da lista, basta utilizar o comando .insert(nº da lista, 'e o desejado')
#ex. lanche.insert(0, 'cachorro-quente')

#Para apagar um elemento de uma lista temos os comandos del, pop, remove
#DEL - ex. del lanche[3], ele deleta pelo indice da lista
#POP - ex. lanche.pop(3), normalmente utilizamos pop para eliminar o último indice da lista, 
# mas também podemos indicar um indice atráves dele.
#REMOVE - ex. lanche.remove('pizza'), o remove ele não utiliza o indice para apagar um item da lista, 
# mas utiliza o nome do item.

# Em todos os casos, o indice é excluido é os indices são nomeados novamente.
#ex. lanche.pop(3), o indice 3 é removido, e o indice 4 se torna o 3, o 5 se torna o 4 e assim sucessivamente.

#Para remover somente o que estiver na lista, podemos utilizar a estrutura if
#ex. if 'pizza' in lanche:
#        lanche.remove('pizza')

#Para fazer uma lista, utilizamos o comando: list(range(a, b))
#ex. valores = list(range(4, 11))

#Para fazer uma lista com valores fora de ordem, utilizamos:
#ex. valores = [8, 2, 5, 4, 9, 3, 0]

#Para deixar esses valores fora de ordem em ordem corretamente podemos utilizar o comando .sort():
#ex. valores = [8, 2, 5, 4, 9, 3, 0]
#ex. valores.sort()

#Para deixar esses valores em ordem reversa, podemos utilizar também o .sort():
#ex. valores = [8, 2, 5, 4, 9, 3, 0]
#ex. valores.sort()
#ex. valores.sort(reverse=True)

#É para saber o tamanho de uma lista podemos utilizar o Len:
#ex. len(valores)'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''valores = list()
for cont in range(0, 4):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')'''

'''Quando alteramos uma lista no python e relacionamos ela a outra lista, alterando qualquer uma das duas
ambas vão sofrer a alteração.'''
a = [2, 3, 4, 7]
'''#Para criar uma cópia...'''
'''b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''