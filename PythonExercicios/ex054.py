# Crie um programa que leia o ano de nascimento de sete pessoas.
# no final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas ja sao maiores

from datetime import date

maior = 0
menor = 0

for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa {} :'.format(c)))
    idade = date.today().year - ano
    if idade > 21:
        maior += 1
    else:
        menor += 1

print('Maiores de idade: {}'.format(maior))
print('Menores de idade: {}'.format(menor))