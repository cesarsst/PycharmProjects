
###
# Estrutura de controle: FOR
for c in range(0, 10):          # ele nao considera o ultimo numero
    print('Oi {}'.format(c))
print('Fim')

for c in range(6, 0, -1):        # contagem regressiva
    print(c)

for c in range(1, 7, 2):         # contagem pulando 2 em 2
    print(c)

n = int(input('Digite um numero: '))

for c in range(1, n+1):
    print(c)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passos: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

for c in range(0, 3):
    n = input('Digite um valor: ')
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(s)
