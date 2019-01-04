# Crie um programa onde o usuario possa digitar cinco valores numericos
# e os cadastre em uma lista, ja na posição correta de inserção (sem usar sort)
# no final, mostre a lista ordenada na tela

lista = []
ultimo = 0
for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0:
        lista.append(val)
        ultimo = val
    else:
        for x, y in enumerate(lista):
            if val <= y:
                lista.insert(x, val)
                break
            else:
                lista.append(val)
                break
print(lista)
