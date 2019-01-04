# Crie um programa onde o usuario digite uma expressao qualquer
# que use parenteses. Seu aplicativo devera analisar se a expressao
# passada esta com os parenteses abertos e fechados na ordem correta

count = 0
exp = str(input('Digite uma expressão: '))
for c, y in enumerate(exp):
    if y == '(':
        count += 1
    elif y == ')':
        count -= 1
if count == 0:
    print('Os parênteses estao abertos e fechados CERTO!')
else:
    print('Os parênteses estao abertos e fechados ERRADO!')