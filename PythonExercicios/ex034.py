# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
# Para salarios superior a 1250, calcule um aumento de 10%
# para os inferiores, o aumento é de 15%

sal = float(input('Digite o valor do salario:'))

if sal > 1250:
    sal = sal + ((sal/100)*10)
else:
    sal = sal + ((sal/100)*15)

print('Seu novo salario é de: {}'.format(sal))