# Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# um dicionario, incluindo o total de gols feitos durante o campeonato

jogador = {}

jogador['nome'] = str(input('Digite o nome: '))
jogador['partidas jogadas'] = int(input('Partidas jogadas: '))

gols = []
total = 0
for c in range(0, jogador['partidas jogadas']):
    gols.append(int(input(f'Gols na partida {c+1}: ')))
jogador['gols partida'] = gols[:]
jogador['total de gols'] = sum(gols)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('{}'.format('#'*50))

print(f"O jogador {jogador['nome']} jogou {jogador['partidas jogadas']} partidas.")
for i, v in enumerate(jogador['gols partida']):
    print(f"Na partida {i+1}, fez {v} gols.")
print(f"Foi um total de {jogador['total de gols']} gols.")
