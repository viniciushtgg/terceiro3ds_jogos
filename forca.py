import random 

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    # Abrir e fechar arquivos com as palavras secretas
    arquivo = open("palavras.txt", "r")

    palavras = []
    #criar uma lista e fazer um laço, 
    # acessando cada linha e guardando-as nessa lista:
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()
     
    numero = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False

    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        # Pedir pro usuario digitar uma letra
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta :
            # Laço for para descobrir se o chute contem
            # na palavra secreta
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = letra
                
                index += 1
        else:
            # A cada letra errada aumenta o numero de erros
            erros += 1

        # Se o erro for igual a 6, o usuario enforcou
        enforcou = erros == 6
        # Se não houver mais "_" o jogador acertou a palavra
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    print("Fim do jogo")

#Só executa esta parte quando
# é executado pelo próprio arquivo,
# ou seja, no forca.py
if (__name__ == "__main__"):
    jogar()


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, voce foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /")