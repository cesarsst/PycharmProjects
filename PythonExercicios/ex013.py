#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite o salário: '))
new_sal = sal + ((sal/100)*15)

print('O novo salario com 15% de aumento é de {}'.format(new_sal))
