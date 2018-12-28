# Estruturas compostas - Tuplas


lanches = ('Hamburger', 'Suco', 'Pizza', 'Pudim') # entre () são TUPLAS

print(lanches)
print(sorted(lanches)) # Ordena a tupla, porem nao muda!
print(lanches[0:2]) # o ultimo elemento especificado no corte é ignorado
print(lanches[1:])  # do elemento 1 ate o final
print(lanches[:2])  # do inicio até o elemento 2 (ignora elemento 2)
print(lanches[-1])  # ultimo elemento
print(lanches[-2])  # penultimo elemento
print(lanches[-3:])  # escreve do -3 até o final (-1)
print(len(lanches)) # Comprimento da tupla lanches

for c in range(0, len(lanches)):
    print(lanches[c], end=' ')

print('\n')

# outra forma -> dessa forma nao temos a posição
for c in lanches:           # Dessa forma não precisa saber o tamanho da tupla
    print(c, end=' ')

# para ter posição
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

# As tuplas são imutaveis!
#   lanches[1] = 'refrigerante' -> nao permite
#   print(lanches[1])

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b               # junta as tuplas em outra
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5))       # conta quantas vezes o numero 5 está dentro de c
print(c.index(8))       # mostra em qual posição está o 8 em c -> pega a primeira ocorrencia
print(c.index(5, 1))    # mostra a a posição em que o 5 aparece, a partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99.88)    # podemos usar tipos diferentes nas tuplas
# del(pessoa)                             # apaga a tupla pessoas (so pode apagar a tupla inteira)
print(pessoa)

