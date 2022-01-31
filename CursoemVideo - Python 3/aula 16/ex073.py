# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio',
        'Athletico Paranaense', 'Santos', 'São Paulo', 
        'Internacional', 'Fluminense', 'Corinthians', 
        'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro',
        'Atlético Goianiense', 'Chapecoense', 'Botafogo', 
        'Vasco da Gama', 'Red Bull Bragantino')
print('=-=' * 53)
print('Lista de Times:')
for t in times:
    print(t, end=' | ')
#print(f'Lista de times do Brasileirão: {times}')
print('\n=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=')
print(f'Os 5 primeiros são: {times[:5]}')
print('=-=' * 53)
print(f'Os 4 últimos são: {times[16:]} ')
print('=-=' * 53)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-=' * 53)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
