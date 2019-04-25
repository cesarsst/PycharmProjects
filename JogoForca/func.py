def geraPalavra():
    from random import randint

    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            result = list(linha.split()[0].upper())
            palavras.append(result)

    totalPalavras = len(palavras)

    return palavras[randint(0, totalPalavras-1)]



geraPalavra()
