# Faça um programa que leia o nome completo de uma pessoa, mostrando
# o primeiro e o ultimo nome separadamente
# Ex: Ana maria de Souza
# primeiro: Ana
# Segundo: Souza

nome = input('Digite um nome: ')
nome = nome.split()
r = len(nome)
print('Primeiro: {} \n Ultimo: {}'.format(nome[0], nome[r-1]))
