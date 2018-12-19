# Crie um programa que leia o nome completo de uma pessoa e mostre



frase = input('Digite seu nome completo: ')
#Outra forma
# frase = str(input('Digite seu nome completo:')).strip()   -> faz o corte direto

# O nome com todas as letras maiusculas
print(frase.upper())

# O nome com todas letras minusculas
print(frase.lower())

# Quantas letras ao total sem considerar espaços
total = len(frase)
esp = frase.count(' ')
result = total - esp
print(result)
    # simplificando print('Seu nome tem ao total {} letras'.format(len(nome)-nome.count(' ')))


# Quantas letras tem o primeiro nome
r = frase.split()
print(len(r[0]))
