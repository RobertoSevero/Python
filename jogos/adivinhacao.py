import random

def jogar():

    print("**********************************")
    print("Bem vindo no jogo de Advininhação!")
    print("**********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nível = int(input("Define o nível: "))

    if(nível == 1):
        total_de_tentativas = 20
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas +1):
        print(numero_secreto)
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!.".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que do que o numero secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor que do que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()