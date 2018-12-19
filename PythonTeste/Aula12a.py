# Condições aninhadas

nome = str(input('Qual é seu nome: '))

if nome == 'Cesar':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paulo'or nome == 'Paulo':
    print('Seu nome é bem popular no brasil!')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino')
else:                                                       # Else é opcional
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}'.format(nome))