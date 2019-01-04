# Estrutura Compostas - Listas

lista = ['0', '1']
lista.append('2')       # comando para adicionar na lista
lista.insert(0,'3')     # adiciona uma posição no espaço 0, e adiciona
del lista[2]            # deleta um posição da lista
lista.pop(2)            # outra forma de deletar -> geralmente para retirar o ultimo (sem parametro)
if '0' in lista:        # se 0 estiver na lista
    lista.remove('0')   # remove elemento na lista pelo conteudo, que encontrar primeiro.
print(lista)

valores = list(range(4, 11))    # cria uma lista de 4 ate 10
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                  # ordena a lista
valores.sort(reverse=True)     # ordena em ordem reversa
len(valores)                    # tamanho da lista
print(valores)

for c,v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}')

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

a = [2, 3, 4, 7]
b = a               # o python cria um ligação entre as listas
b[2] = 8            # logo tanto lista a quanto b tem o valor alterado
print(a)
print(b)

# para fazer um copia de a para b
b = a[:]                # cria copia
b[2] = 8
print(a)
print(b)