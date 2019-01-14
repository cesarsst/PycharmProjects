# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios
# Guarde esses resultados em um dicionário. No final coloque esse dicionario em
# ordem sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep

result = {'Player1': randint(1,6), 'Player2': randint(1,6), 'Player3': randint(1,6), 'Player4': randint(1,6)}
maior = 0
aux = 0
for k, v in result.items():
    print(f'O {k} tirou {v}')
    sleep(1)

    if maior == 0:
        maior = k
        print(k)





