def aumentar(n, y):
    n = n + ((n*y)/100)
    new = str(f'R$:{n},00')
    print(f'% com Aumento no valor {new}')


def diminuir(n, x):
    n = n - ((n*x)/100)
    new = str(f'R$:{n},00')
    print(f'% com descrecimo no valor {new}')


def dobro(n):
    new = str(f'R$:{n*2},00')
    print(f'Dobro do valor {new}')


def metade(n):
    new = str(f'R$:{n/2},00')
    print(f'Metade do valor {new}')


def resumo(n, x, y):

    print('Funções implantadas: \n'
          'n =  valor  \n '
          'x = % para aumento) \n'
          'y = % para descrecimo \n')
    metade(n)
    dobro(n)
    diminuir(n, y)
    aumentar(n, x)