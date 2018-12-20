### faça um programa que calcule a soma entre todos os numeros
# impares que sao multiplos de 3 e que encontram entre o
# intervalo de 1 ate 500###

soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
print(soma)

