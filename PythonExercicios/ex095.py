# Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
# a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# um dicionario, incluindo o total de gols feitos durante o campeonato

jogadores = []
info = {}
gols_partida = []
while True:
    gols_partida.clear()
    info.clear()
    info['nome'] = str(input('Nome: '))
    total_partida = int(input(f"Quantas partidas {info['nome']} jogou? "))
    for i in range(0, total_partida):
        gols_cont = (int(input(f"Quantos gols na partida {i}? ")))
        gols_partida.append(gols_cont)
    info['gols'] = gols_partida.copy()
    info['total'] = sum(gols_partida)
    jogadores.append(info.copy())

    resp = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break

print("{:<10} {:<20} {:<20} {:<20} ".format('Cod', 'Nome', 'Gols', 'Total'))
for i, p in enumerate(jogadores):
    print('{:<10} {:<20} {} {:>20}'.format(i, p['nome'], p['gols'], p['total']))

while True:
    pesq = int(input('Digite o codigo para mais informação do jogador: '))
    if pesq >= len(jogadores) or pesq < 0:
        print(f'Erro Não existe jogador com código {pesq}!')
    else:
        print(f"Dados do Jogador:  {jogadores[pesq]['nome']} ")
        for i in range(0, len(jogadores[pesq]['gols'])):
            print(f"No jogo {i} fez {jogadores[pesq]['gols'][i]}")

    resp = str(input('Deseja pesquisa outro jogador? [S/N]')).upper().split()[0]
    if resp == 'N':
        break

