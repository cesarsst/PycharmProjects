# Faça um programa que tenha uma função chamada maior(), que receba
# varios parametros com valores inteiros
# seu programa tem que analizar todos os valores e dizer qual é o maior deles


def maior(* num):
    cont = 0
    maior = 0
    if cont == 0:
        maior = num[0]
    while cont < len(num):
        for valor in num:
            if valor > maior:
                maior = valor
            cont += 1
    print(f'O maior valor foi {maior} de um total de {cont} elementos!')

maior(2, 5, 1, 10, 9)
maior(19, 20, 100, 12, 13)
maior(100, 10, 20)
maior(1, 19, 100)