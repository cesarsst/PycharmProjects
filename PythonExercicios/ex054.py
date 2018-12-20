# Crie um programa que leia o ano de nascimento de sete pessoas.
# no final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas ja sao maiores

maior = 0
menor = 0

for c in range(1,8):
    idade = int(input('Digite a idade da pessoa {} :'.format(c)))
    if idade > 21:
        maior += 1
    else:
        menor += 1

print('Maiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))