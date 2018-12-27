# Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA
# mostrando os 10 primeiros termos da progressao usando a estrutura
# while

primeiro = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
pa = primeiro

c = 10
while c != 0:
    print('{} '.format(pa), end ='')
    pa += razao
    c -= 1
print('Fim')