# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios
# Guarde esses resultados em um dicionário. No final coloque esse dicionario em
# ordem sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter

result = {'Player1': randint(1, 6),
          'Player2': randint(1, 6),
          'Player3': randint(1, 6),
          'Player4': randint(1, 6)}

for k, v in result.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(result.items(), key=itemgetter(1), reverse=True)
print('Ranking: ')
# Temos que tratar como uma lista
for i, v in enumerate(ranking):
    print(f'{i+1}° {v[0]} com {v[1]}')




