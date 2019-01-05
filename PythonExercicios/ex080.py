# Crie um programa onde o usuario possa digitar cinco valores numericos
# e os cadastre em uma lista, ja na posição correta de inserção (sem usar sort)
# no final, mostre a lista ordenada na tela

lista = []
ultimo = 0
for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0 or val >= ultimo:
        lista.append(val)
        print(f'Valor adicionado ao final da lista...')
        ultimo = val
    else:
        for x in range(0, len(lista)):
            if val <= lista[x]:
                lista.insert(x, val)
                print(f'Adicionado na posição {x} da lista...')
                break
print(lista)

# outra forma

list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(list)

