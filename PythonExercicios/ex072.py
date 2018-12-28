# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extensao de zero ate vinte
# seu programa deverá ler um numero pelo teclado (entre 0 e 20)
# e mostra-lo por extenso

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


n = -1
while n < 0 or n > 20:
    n = int(input('Digite um numero entre 0 e 20: '))

print(f'Você digitou o numero {contagem[n]}')