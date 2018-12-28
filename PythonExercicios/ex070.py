# Crie um programa que leia o nome e o preço de varios produtos
# O Programa deverá perguntar se o usuario vai continuar
# No final mostre:
#   a) Qual é o total da compra
#   b) Quantos produtos custam mais de 1000
#   c) Qual é o nome do produto mais barato

total = prod = menor = 0
while True:
    #Lendo valores
    nome = str(input('Digite o nome do produto: '))
    prec = float(input('Digite o valor do produto R$: '))

    #Total Gasto
    total += prec
    #Qtd de Produtos acima de 1000 reais
    if prec > 1000:
        prod += 1
    #Nome do produto mais barato
    if menor == 0:
        menor = prec
        men_prod = nome
    else:
        if prec < menor:
            menor = prec
            men_prod = nome

    # Perguntando continuidade ao usuario
    resp = ' '
    while resp not in 'SN' :
        resp = str(input('Deseja cadastrar mais produtos? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f"""O total gasto foi de: {total}
A quantidade de produtos acima de R$:1000,00 é de {prod}
O nome do produto mais barato é {men_prod} e custou R$:{menor}""")