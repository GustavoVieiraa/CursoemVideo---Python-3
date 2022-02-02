#Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita 
# que o usuário possa mostrar as notas de cada aluno individualmente.
print('=-=' * 20)
print(' ' * 18 + 'Boletim escolar - 2022')
print('=-=' * 20)
lista_info = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista_info.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'S':
        print('=-=' * 20)
    if resp == 'N':
        break
print('=-=' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-=' * 25)
for i, a in enumerate(lista_info):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=-=' * 15)
    oc = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if oc == 999:
        print('FINALIZANDO... ')
        break
    if oc <= len(lista_info) - 1:
        print(f'Notas de {lista_info[oc][0]} são {lista_info[oc][1]}')
print('=-=' * 30)