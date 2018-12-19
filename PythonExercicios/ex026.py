# Faça um programa que leia uma frase pelo teclado e mostre:
# Qts vezes aparece a letra 'A'
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase qualquer: ')).upper().strip()


print('A letra A aparece {} vezes '.format(frase.count('A')))

print('A primeira posição em que a letra A aparece é {}'.format(frase.find('A')+1))

print('O ultimo A aparece na posição {}'.format(frase.rfind('A')))
