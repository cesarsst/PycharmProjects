# Cire uma tupla preenchida com os 20 primeiros colocados da tabela
# do campeonato brasileiro de futebol, na ordem de colocação. Depois
# mostre:
# a) apenas os 5 primeiros colocados da tabela
# b) os ultimos 4 colocados da tabela
# c) uma lista com os times em ordem alfabetica
# d) Em que posição na tabela está o time da chhapecoense

tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',
          'São Paulo', 'Atlético', 'Atletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
          'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
# Item A
for c in range(0,5):
    print(f'Colocação: {c+1}° | Time: {tabela[c]}')
# Item B
print('\n')
print('Ultimos colocados:')
for c in range(-4, 0, 1):
    print(f'Colocação: {tabela.index(tabela[c])+1}°', tabela[c])
# Item C
print('\n')
for c in sorted(tabela):
    print(c, end=' -> ')
print('Fim')
# Item D
print('Chapecoense está na {}° colocação'.format(tabela.index('Chapecoense') + 1))
