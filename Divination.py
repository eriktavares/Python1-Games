import random

def play():
    print("Bem vindo")
    print("================")

    secretNumber = (random.randrange(1, 101))

    print("Qual a Dificuladade")
    print("(1) Fácil (2) Médio (3) Díficil")
    level = int(input("Defini Nível: "))

    if(level==1):
        attemps=20
    elif(level==2):
        attemps=10
    else:
        attemps=5


    for roundvar in range(1, attemps+1):
        kick = input("Digite o seu numero entre 1 e 100: ")
        print("vc digitou {} de Tentativa {}".format(kick ,roundvar))
        kickInt = int(kick)

        if(kickInt<1 or kickInt>100):
            print("Numero invalido")
            continue

        if (secretNumber == kickInt):
            print("vc acertou", secretNumber)
            break
        else:
            if (kickInt > secretNumber):
                print("vc errou, chute menor")
            elif (kickInt < secretNumber):
                print("vc errou, chute maior")
        roundvar =roundvar +1

    print("Fim do Jogo")

if(__name__=='__main__'):
    play()

