def jogar():
    print("*********************************\n")
    print("Bem vindo ao jogo da forca!\n")
    print("*********************************\n")

    palavra_secreta = "laranja".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("A palavra secreta contem: {}\n".format(letras_acertadas))
    while not acertou and not enforcou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    print("\nEncontrei as letras na posição {}\n".format(letras_acertadas))
                index += 1

            acertou = "_" not in letras_acertadas
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))
            enforcou = (erros == 6)

    print("\nFim do jogo\n")
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu")


if __name__ == "__main__":
    jogar()
