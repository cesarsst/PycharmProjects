# Crie um programa que leia a IDADE e o SEXO de varias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar se o usuario
# quer ou nao continuar, no final mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

#iniciando variaveis acumuladoras
maiores = homens = mulheres = 0

while True:
    # Entrando com dados de cadastro:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]')).strip().upper()[0]

    #Verificando condições
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    # Verifica se quer cadastrar mais
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais algumas pessoa? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
# Resultados
print(f'Pessoas maiores de 18 anos: {maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menores de 20 anos: {mulheres}')