# crie um programa que leia varios numeros inteiros pelo teclado
# no final da execução, mostre a media entre todos os valores e qual
# foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valroes

soma = 0
maior = 0
menor = 0
count = 0
resp = '1'
while resp != 'n':
    n = int(input('Digite um numero: '))
    if count == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    soma += n
    count += 1
    resp = str(input('Deseja continuar? [s/n]').lower())

print('Média: {}'.format(soma/count))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
