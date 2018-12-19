# Escreva um programa que leia a velocidade de um carro
# Se ele utrapassar 80km/h, mostre uma mensagem dizendo que foi multado
# A multa vai custar 7 reais por cada km acima do limite

vel = float(input('Qual é a velocidade do carro?: '))

if vel <= 80:
    print('Parabéns, você está dentro da velocidade')
else:
    print('Você foi multado!')
    multa = (vel - 80)*7
    print('Você foi multado em: R$:{}'.format(multa))
