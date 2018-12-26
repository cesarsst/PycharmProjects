# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
# no final mostre:
# A media da idade, nome do homem mais velho, e qts mulheres tem menos de 20 anos

# Listas que iram armazenar os dados
nomes = []
idades = []
sexos = []

for c in range(0, 4):
    print('{} {}° pessoa {}'.format('='*10, c+1, '='*10))
#Coletando dados
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo  M - masculino  F - feminino: ')).strip().lower()
# Gravando dados na listas
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo.lower())

# calculo da media do grupo
med_idade = 0
for c in range(0, 4):
    med_idade += idades[c]
print('Média das idades: {}'.format(med_idade/4))

# Procurando homem mais velho:
maior = 0
for c in range(0, 4):
    if sexos[c] == 'm':
        if maior == 0:
            maior = idades[c]
        else:
            if idades[c] > maior:
                maior = idades[c]
                resp = nomes[c]
print('Nome do homem mais velho é {} e tem {} anos'.format(resp, maior))

# Procurando mulheres menores de 20 anos
f_count = 0                 # variavel que armazena qtd de mulheres com menos de 20 anos
for c in range(0, 4):
    if sexos[c] == 'f':
        if idades[c] < 20:
            f_count += 1
print('Quantidade de mulheres abaixo de 20 anos: {} '.format(f_count))