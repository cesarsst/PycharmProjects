# Crie um programa que tenha uma tupla com varias palavras (nao usar acento)
# Depois disso, você deve mostrar, para cada palavra quais são suas vogais

tupla = ('ola', 'cesar', 'batata', 'python')

tam = len(tupla)
print(tam)

for c in range(0, tam):
    pal = tupla[c]
    tam_pal = len(tupla[c])             # Tamanho da palavra atual
    print(f'Na palavra: {pal} temos as  vogais: ', end=' ')
    for i in range(0, tam_pal):
        if pal[i] in 'aeiouAEIOU':
            print(pal[i], end=' ')
    print('\n')

# Outra forma.Quando n precisa de posição é mais eficiente!

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')