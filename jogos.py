import forca
import advinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")


    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        advinhacao.jogar()

#Só executa esta parte quando
# é executado pelo próprio arquivo,
# ou seja, no jogos.py
if (__name__ == "__main"):
    escolhe_jogo()