# Crie um programa que leia varios numeros e coloque em uma lista
# depois disso mostre:
# A) quantos numeros foram digitados
# b) A lista de valores ordenada de forma decrescente
# c) se o valor 5 foi digitado e esta ou nao na lista

lista = []
while True:
    val = int(input('Digite um valor: '))
    lista.append(val)
    resp = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break

print(f'Numeros digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista em ordem descrecente {lista}')
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
