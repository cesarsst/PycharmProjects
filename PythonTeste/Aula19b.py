brasil = []

estado = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

brasil2 = []
state = {}
for c in range(0, 3):
    state['uf'] = str(input('Unidade Federativa: '))
    state['sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(state.copy())

print(brasil)

for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil2:
    for v in e.values():
        print(v, end='')
    print()