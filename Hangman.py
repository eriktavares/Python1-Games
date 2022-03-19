
def play():
    print("===================================")
    print("*********** Bem vindo**************")
    print("===================================")
    print("===========Fim de Jogo=============")
    secret_word="banana"

    correctWords =["_","_","_","_","_","_"]
    print(correctWords)
    hanged=False
    hit=False

    index=0
    while(not hanged or not hit):
        kick=input("Qual a Leta?")
        for letra in secret_word:
            if(kick.upper()==letra.upper()):
                correctWords[index]= letra
            index=index+1
        print(correctWords)

if(__name__=="__main__"):
    play()

