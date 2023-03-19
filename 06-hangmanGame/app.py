import random


palavras = ["banana", "abacaxi", "melancia", "uva", "laranja"]
boneco = [
    '  _____',
    '  |/    |',
    '  |     O',
    '  |    /|\\',
    '  |    / \\',
    ' _|_',
    '|   |______',
    '|          |',
    '|__________|'
]


def imprimir_boneco(tentativas_restantes):
    for linha in boneco[:6 - tentativas_restantes]:
        print(linha)


def imprimir_palavra_a_ser_advinhada(letras_adivinhadas):
    print(' '.join(letras_adivinhadas))


def jogar(palavra):
    tentativas_restantes = 6
    letras_advinhadas = ['_' for letra in palavra]

    while True:
        imprimir_palavra_a_ser_advinhada(letras_advinhadas)

        letra = input('Digite uma letra: ')

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_advinhadas[i] = letra
        else:
            tentativas_restantes -= 1
            imprimir_boneco(tentativas_restantes)

        if '_' not in letras_advinhadas:
            print("Parabéns, você acertou a palavra: '{}'".format(palavra))
            break
        elif tentativas_restantes == 0:
            print("Você perdeu! A palavra era '{}'".format(palavra))
            imprimir_boneco(tentativas_restantes)
            break


palavra = random.choice(palavras)
jogar(palavra)
