# Nessa aula, vamos aprender como utilizar a instrução break e 
# os loopings infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Python, 
# já que em alguns casos precisamos interromper um laço no meio do caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
from time import sleep
n = s = 0
while True:
    n = int(input('Informe um número: '))
    if n == 999:
        sleep(5)
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
