# Crie um programa que leia varios numeros inteiros pelo teclado
# O programa só vai parar quando o usuario digitar o valor 999, que
# é a condição de parada. No final, mostre quantos numeros foram
# digitados e qual foi a soma entre eles (desconsiderando o 999 -flag)

soma = cont = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores digitado é {soma}')