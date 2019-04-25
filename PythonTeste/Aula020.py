# Estruturas compostas - Função

def returnn():
    return(0)

def mostraLinha():
    print('-------------------------------------')

mostraLinha()
print('{:^37}'.format('Titulo'))
mostraLinha()

def mensagem(msg):
    print('-------------------------------------')
    print('{:^37}'.format(msg))
    print('-------------------------------------')

mensagem('Titulo Editavel')
mensagem('Titulo Editavel 2')

#retornando um valor de uma função
var = returnn()
print(var)

def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(s)
soma(3, 6)
soma(b=5, a=8)  #passando parametro como argumento

# empacotando parametros - passa todos parametros como uma tupla
def contador(* num):
    print(num)
    for valor in num:
        print(valor)

contador(3, 4, 5, 6)
contador(1, 3, 4)

def dobra(lst):
    for i in range(0, len(lst)):
         lst[i] *= 2
    print(lst)
valores = [7, 2, 5, 0, 4]
dobra(valores)

def somar(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Soma dos valores: {s}')

somar(5, 2)
somar(3, 5, 8)