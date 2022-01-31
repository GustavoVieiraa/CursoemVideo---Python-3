# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.
# Tuplas são imutáveis
# Estrutura composta

#pessoa = ('Gustavo', 39, 'M', 99.88)
# Del serve para apagar da memoria
#print(pessoa) 
#del (pessoa)



#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)
#print(c.index(5))

# Count para localizar números ou variaveis na Tupla como quantas vezes apareceu
#print(c.count(9))


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Coca-Cola')
#print(sorted(lanche))
#print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}')

#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
   #print(f'Eu vou comer {comida} na posição {pos}')

