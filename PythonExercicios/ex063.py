# Escreva um programa que leia um numero N inteiro e mostre na tela
# os n primeiros elementos de uma sequencia de fibonacci

n = int(input('Digite um valor qualquer: '))
atual = 1
ant = 0
aux = 0
while n != 0:
    print('{} '.format(atual), end='')
    aux = atual
    atual = atual + ant
    ant = aux
    n -= 1