#Crie um programa onde o usuário digite uma 
# expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão 
# passada está com os parênteses abertos e fechados na ordem correta.
print('~~' * 20)
print(' ' * 5 + 'VALIDANDO EXPRESSÕES MATEMÁTICAS')
print('~~' * 20)
aberto_parentes = []
fechado_parentes = []
parentes = str(input('Informe uma expressão: '))
for fat in parentes:
    for partes in fat:
        if partes == '(':
            aberto_parentes.append(partes)
        if partes == ')':
            fechado_parentes.append(partes)
if len(aberto_parentes) == len(fechado_parentes):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
print('~~' * 20)