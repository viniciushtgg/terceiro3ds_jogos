def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"

    acertou = False
    enforcou = False

    while not acertou and not enforcou:
        # Pedir pro usuario digitar uma letra
        chute = input("Qual letra?")

        # Laço for para descobrir se o chute contem
        # na palavra secreta
        index = 0
        for letra in palavra_secreta:
            if letra == chute:
                print("Encontrei a letra {} na posição {}".format(letra, index))
            
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

#Só executa esta parte quando
# é executado pelo próprio arquivo,
# ou seja, no forca.py
if (__name__ == "__main__"):
    jogar()