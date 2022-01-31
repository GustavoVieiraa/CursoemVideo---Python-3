# //Crie um programa que leia duas notas de um aluno e 
# calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
print('=-=' * 7 + 'SYSTEM MEDIA' + '=-=' * 7)
n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
m = (n1+n2) / 2
if m >= 7:
    print('=========APROVADO=========')
    print('|NOTAS| {:.1f} e {:.1f}, a sua média foi {:.1f}'.format(n1, n2, m))
    print('==========================')
elif m > 5.1 and m < 6.9:
    print('=========RECUPERAÇÃO=========')
    print('|NOTAS| {:.1f} e {:.1f}, a sua média foi {:.1f}'.format(n1, n2, m))
    print('=============================')
elif m < 5:
    print('=========REPROVADO=========')
    print('|NOTAS| {:.1f} e {:.1f}, a sua média foi {:.1f}'.format(n1, n2, m))
    print('===========================')
