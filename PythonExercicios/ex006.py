#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada

n = int(input('Digite um valor: '))
d = n*2
t = n*3
rq = n**(1/2)

print('O dobro de {} é {} , seu triplo é {} e sua raiz quadrada é {}'.format(n, d, t, rq))
