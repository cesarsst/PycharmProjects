# Escreva um programa que leia um numero inteiro qualquer e peça
# para o usuario escolher qual sera a base de conversao:
# 1- binario 2- octal 3- hexadecimal

num = int(input('Digite um numero inteiro: '))
print('1- Decimal \n 2- Octal \n 3-Hexadecimal')
op = int(input('Digite para qual base deseja converter: '))

if op == 1:
    print(bin(num)[2:])
elif op == 2:
    print(oct(num)[2:])
elif op == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida!')

# Conversao para binario na raça
# resp = []
#     while num != 0:
#         conv = num % 2
#         resp.append(conv)
#         num = int(num/2)
#     resp.reverse()
#     print(resp)