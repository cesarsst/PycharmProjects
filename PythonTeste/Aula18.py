#Estrutura composta - lista 2

dados = ['Pedro', '25']
pessoas = []

pessoas.append(dados[:])
print(pessoas)

pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas2)

print(pessoas2[0][0])
print(pessoas2[1][1])
print(pessoas2[1])

teste = list()
teste.append('Cesar')
teste.append(40)
galera = list()
galera.append(teste[:]) # necessario fazer copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

for p in galera:    # varendo lista
    print(f'Nome: {p[0]} Idade: {p[1]}')

# Lista dentro de lista
lista = []
dado = []
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear()                        #limpa para nao duplicar no append
print(lista)

for p in lista:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores!')