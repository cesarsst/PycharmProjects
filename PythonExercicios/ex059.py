# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 soma
# 2 multiplicar
# 3 maior
# 4 novas numeros
# 5 sair do programa
# Seu programa devera realizar a operação solicitada em cada caso


n1 = int(input('Digite o valor um: '))
n2 = int(input('Digite o valor dois: '))

c = 0
while c != 5:
    print("""Qual operação você deseja fazer? 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair: """)
    c = int(input())

    if c == 1:
        print('Soma de {} + {} = {}'.format(n1, n2, n1+n2))
    elif c == 2:
        print('A multiplicação de {} * {} = {}'.format(n1, n2, n1*n2))
    elif c == 3:
        if n1 > n2:
            print('Maior valor: {}'.format(n1))
        else:
            print('Maior valor: {}'.format(n2))
    elif c == 4:
        print('Digite novos numeros para numero um e numero dois:')
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
    elif str(c) not in '12345':
        print('Opção inválida!')