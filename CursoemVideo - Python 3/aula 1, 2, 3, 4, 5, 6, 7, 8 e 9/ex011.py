# //Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
L = float(input('Qual a largura da parede: \n'))
A = float(input('Qual a altura da parede: \n'))
Mquad = (L * A)
T = (Mquad/2)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(L, A, Mquad))
print('A quantidade necessária de litros de tinta para pintar é {}lts:'.format(T))
