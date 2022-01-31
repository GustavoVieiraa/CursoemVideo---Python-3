# Crie um programa que tenha uma tupla com várias palavras. (Não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for dicionario in palavras:
    print(f'\nNa palavra {dicionario.upper()} temos ', end='')
    for letra in dicionario:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            