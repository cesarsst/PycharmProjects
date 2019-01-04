# Crie um programa para ler varios numeros e colocar em uma lista
# depois disso, crie duas listas extras que vao conter apenas os valores
# pares e os valores impares digitados respectivamentes
# ao final mostre o conteudo das tres listas geradas

lista = []
impar = []
par = []
while True:
    val = int(input('Digite um valor: '))
    lista.append(val)
    resp = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break

for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'Lista Original: {lista} \nPares: {par}\nImpar: {impar}')