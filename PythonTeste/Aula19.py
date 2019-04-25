dados = {'nome': 'cesar', 'idade': 21}
print(dados['nome'])

dados['sexo'] = 'M'     # para adicionar ao dicionario
print(dados)

del dados['idade']
print(dados)

filme = {
    'titulo':'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas'
}

print(filme.values())       # seleciona dados
print(filme.keys())         # seleciona chaves
print(filme.items())        # seleciona os dois anteriores

for k, v in filme.items():
    print(f'O {k} é {v}')

for k in filme.values():    # printa os valores
    print(k)

for k in filme.keys():      # printa as keys
    print(k)

locadora = []
locadora.append(filme)
print(locadora)
print(locadora[0]['ano'])
print(f'O {filme["titulo"]} é do ano de {filme["ano"]}')
filme['ano'] = 2000
print(filme)
