# Operadores Aritiméticos

#   +     adição
#   -     substração
#   *     multiplicação
#   /     divisao
#   **    potencia              outra forma-> pow(4,3) == 4**3
#   //    divisao inteira
#   %     resto da divisao

# Ordem de precedência
#   1     ()
#   2     **
#   3     * e / e // e %
#   4     + e -

# Prática

# Como calcular raiz quadrada? 81**(1/2)
# e raiz cubica? 81**(1/3)
# Podemos multiplicar strings? Ex: 'oi'*5, "="*20, print('='*20)

# Exemplos

nome= input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))      # Escreve o nome em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome))     # Escreve o nome em 20 espaço alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome))     # Escreve o nome em 20 espaço alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))     # Escreve o nome em 20 espaço centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))    # Escreve o nome em 20 espaço centralizado entre =

# Ex 2
n1 = int(input("Um valor: "))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
dr = n1 % n2

print('A soma vale {} \n A multiplicação vale {} \n A divisao vale {:.3f} \n A divisao inteira vale {} \n A exponenciacao vale {} \n O resto da divisao é {}'.format(s, m, d, di, e, dr))

# usando {:.3f} aparece somente 3 casas depois da virgula

