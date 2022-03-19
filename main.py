# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Hangman
import Divination


def play():
    print("Bem Vindo !!")
    game = int(input("Qual jogo vc quer jogar (1) Advinhação e 2 Forca \n"))
    if(game==1):
        Divination.play()

    if(game==2):
        Hangman.play()


play()