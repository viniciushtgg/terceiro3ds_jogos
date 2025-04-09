def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_","_","_","_",]

    acertou = False
    enforcou = False

    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        # Pedir pro usuario digitar uma letra
        chute = input("Qual letra?")
        chute.strip()

        if chute in palavra_secreta :
            # Laço for para descobrir se o chute contem
            # na palavra secretab
            index = 0
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():
                    letras_acertadas[index] = letra
                
                index += 1
        else:
            # A cada letra errada aumenta o numero de erros
            erros += 1

        # Se o erro for igual a 6, o usuario enforcou
        enforcou = erros == 6
        print(letras_acertadas)

    print("Fim do jogo")

#Só executa esta parte quando
# é executado pelo próprio arquivo,
# ou seja, no forca.py
if (__name__ == "__main__"):
    jogar()