# Crie um programa onde o usuario possa digitar varios valores
# numericos e cadastreos em uma lista
# caso o numero ja exista, ele não sera adicionado
# no final, serao exibidos todos os valores unicos digitados em ordem
# crescente

lista = []
while True:
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print('Valor Adicionado')
    else:
        print('Valor duplicado! Não adicionado!')
    resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break
lista.sort()
print(f'{lista}')