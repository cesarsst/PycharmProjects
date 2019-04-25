# Faça um programa que tenha uma lista chamada numeros e duas funções
# chamada sorteia() e somaPar().
# A primeira função vai sortear 5 numeros e vai colocar-los dentro da lista
# e a segunda função vai mostrar a soma entre os valores pares sorteados pela
# função anterior

numeros = []

def sorteia():
    from random import randint
    lst = []
    for i in range(0, 5):
        lst.append(randint(1, 20))
    return(lst)

def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é: {soma}')

numeros = sorteia()
print(numeros)
somaPar(numeros)