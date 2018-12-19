# Crie um programa que leia duas notas de aluno e calcule sua média
# mostrando uma mensagem no final de acordo com a média atingida
# media abaixo de 5: reprovado
# media entre 5 e 6.9: recuperação
# media >= 7 : aprovado

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2

if m < 5:
    print("Reprovado!")
elif m == 5 or m < 7:
    print('Recuperação!')
else:
    print('Aprovado!')