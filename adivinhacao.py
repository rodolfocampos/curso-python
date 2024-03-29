import random


def jogar():
    imprime_boas_vindas()
    iniciar_jogo()


def imprime_boas_vindas():
    print("*********************************\n")
    print("Bem vindo ao jogo de adivinhacão!\n")
    print("*********************************\n")


def selecionar_dificuldade():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 6
    elif nivel == 3:
        tentativas = 3
    else:
        selecionar_dificuldade()
    return tentativas


def iniciar_jogo():
    numero_secreto = int(random.randint(1, 50))
    pontos = 1000

    total_de_tentativas = selecionar_dificuldade()

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}\n".format(rodada, total_de_tentativas))

        chute = int(input("Digite o um numero entre 1 e 50: "))

        print("\n*********************************\n")
        print("Você digitou {}\n".format(chute))

        if chute < 1 or chute > 50:
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.\n")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = round(abs(numero_secreto - chute))
            pontos = pontos - pontos_perdidos

        if rodada == total_de_tentativas:
            print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
