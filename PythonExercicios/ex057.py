# Faça um programa que leia o sexo de uma pessoa, mas que só aceite
# 'm' ou 'f'. Caso esteja errado, peça a digitação novamente até ter
# um valor correto

c = 0
nome = str(input('Digite o sexo da pessoa [M/F]: ')).lower().strip()[0]
while c != 1:
    if nome != 'f' and nome != 'm':
        nome = str(input('Dados inválidos, digite novamente [M/F]: ')).lower().strip()[0]
    else:
        print('Dado confirmado!')
        c = 1

# outra forma

#sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#while sexo not in 'MmFf':
#    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
#print('Sexo {} registrado com sucesso'.format(sexo))