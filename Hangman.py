import random


def printStartGame():
    print("===================================")
    print("**** Bem vindo ao jogo da Forca ****")
    print("===================================")


def loadSecretWord():


    file = open("palavras.txt", "r")
    words = []
    for line in file:
        line = line.strip()
        words.append(line)
    file.close()

    pos = random.randrange(0, len(words))
    return words[pos].upper()


def starCorretWords(secretWord):
    return ["_" for letter in secretWord]


def kick_input():
    return input("Qual a Leta?").strip().upper()


def correct_letters(kick, secretWord, correctWords):
    index = 0
    for letra in secretWord:
        if (kick == letra):
            correctWords[index] = letra
        index = index + 1


def print_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secretWord):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secretWord))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def draw_handman(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def play():

    printStartGame()
    secretWord=loadSecretWord()


    correctWords = starCorretWords(secretWord)
    print(correctWords)
    hanged=False
    hit=False
    errors=0

    while(not hanged and not hit):
        kick= kick_input()

        if(kick in secretWord):
           correct_letters(kick, secretWord, correctWords)
        else:
            errors=errors+1
            draw_handman(errors)
        hanged=errors==7
        hit= '_' not in correctWords

        print(correctWords)
        if(hit):
            print_winner_message()
            print(hit)
            #break
        if(hanged):
            print_loser_message(secretWord)
            print(hanged)
            #break

if(__name__=="__main__"):
    play()

