import func

print('Jogo da Forca \n'
      'Desenvolvido por: Cesar Soares Stenico \n'
      'Menu: \n'
      '0- Sair \n'
      '1- Aprender a jogar \n '
      '2- Jogar! \n')


tentativa_restante = 6
acertos = 0
palavra_secreta = func.geraPalavra() #função que gera uma palavra aleatoria -> [em lista]
palavra_descoberta = ['-' for letra in palavra_secreta]

print(f'{palavra_descoberta}    Dica: {len(palavra_descoberta)} Letras!')
while tentativa_restante > 0:
    chute = str(input('Digite uma letra: ').upper())
    for i, letra in enumerate(palavra_secreta):
        if chute == letra:
            palavra_descoberta[i] = letra
            acertos += 1
            flag = 1

    print(palavra_descoberta)
    if acertos == len(palavra_descoberta):
        print('Você Ganhou!')
        break

    if flag == 0:
        tentativa_restante -= 1
        print(f'Você errou! Restam {tentativa_restante} tentativas restante!')
    else:
        flag = 0

    if tentativa_restante == 0:
        print('Você perdeu!')
        break
