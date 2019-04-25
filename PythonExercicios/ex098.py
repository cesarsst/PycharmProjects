# Faça um programa que tenha uma função chamada contador(), que
# receba tres parametros: inicio, fim e passo, e realiza a contagem
# Seu programa tem que realizar tres contagem atraves da função
# criada
# a) de 1 ate 10, de 1 em 1
# b) de 10 ate 0, de 2 em 2
# uma contagem personalizada

def contador(inicio, fim, contagem):
    contagem = abs(contagem)
    if inicio < fim:
        for i in range(inicio, fim+1, contagem):
            print(i, end=' ')
    else:
        for i in range(inicio, fim-1, -contagem):
            print(i, end=' ')
contador(1, 10, 1)
print('\n')
contador(10, 1, 2)
print('\n')
print('Digite a forma que você quer contar: ')
inicio = int(input('Numero inicial: '))
fim = int(input('Numero final: '))
contagem = int(input('Pulando em: '))
contador(inicio, fim, contagem)