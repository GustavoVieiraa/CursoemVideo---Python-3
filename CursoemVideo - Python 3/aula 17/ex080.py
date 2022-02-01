#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''                         VARIAVEIS GLOBAIS                      '''
nums = []
print('~~' * 30)
print(' ' * 15 + 'LISTA ORDENADA SEM REPETIÇÕES')
print('~~' * 30)
for c in range(0, 5):
    num = int(input(' ' * 20 + 'Digite um número: '))
    if c == 0 or num > nums[-1]:
        nums.append(num)
    else:
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, num)
                break
            pos += 1
print('~~' * 30)
print(nums)