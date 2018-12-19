# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "SANTO"

nome = str(input('Digite o nome da sua cidade: ')).upper().split()
print('SANTO' in nome[0])


