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
    gol_partida = int(input(f'Gols na partida {c+1}: '))
    gols.append(gol_partida)
    total += gol_partida
jogador['gols partida'] = gols
jogador['total de gols'] = total

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('{}'.format('#'*50))

print(f"O jogador {jogador['nome']} jogou {jogador['partidas jogadas']} partidas.")
for i in range(0, len(gols)):
    print(f"Na partida {i+1}, fez {gols[i]} gols.")
print(f"Foi um total de {jogador['total de gols']} gols.")
