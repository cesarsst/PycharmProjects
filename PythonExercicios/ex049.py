# Refaça  o ex009 mostrando a tabuado de um numero que o usario escolher
# so que agora usando laço for

n = int(input('Digite um numero para ver sua tabuada: '))

for c in range(0,11):
    print('{} x {:2} = {}'.format(n, c, n * c))
