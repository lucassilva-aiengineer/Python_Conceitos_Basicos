import time
import random


def escolher():

    print("Escolha a sua opção (pedra, papel ou tesoura).")

    time.sleep(2)
    escolha_jogador = input("Indique a sua opção: ")

    opcoes_computador = ["pedra", "papel", "tesoura"]

    random.shuffle(opcoes_computador)
    escolha_computador = random.choice(opcoes_computador)

    # Vamos armazenar as nossas escolhas em um dicionario alocado na memória, atribuido a uma variáve. 

    escolhas = {"escolha_jogador": escolha_jogador ,"escolha_computador": escolha_computador}

    return escolhas

def verificar_vencedor(escolhas):

    """ Quando o computad"""

    escolha_jogador = escolhas["escolha_jogador"]
    escolha_computador = escolhas["escolha_computador"]

    # vitorias = {"vitorias_jogador": vitorias_jogador, "vitorias_computador"}

    if not escolha_computador == escolha_jogador.lower(): 

        if escolha_jogador.lower() == "pedra":
            if escolha_computador == "papel": 

                print("Escolha Jogador:", escolha_jogador, "Escolha computador:", escolha_computador)
                print("O computador venceu!")

                return 0

            elif escolha_computador == "tesoura":

                print("Escolha Jogador:", escolha_jogador, "Escolha computador:", escolha_computador)
                print("Você venceu!")

                return 1

        elif escolha_jogador.lower() == "papel":
            if escolha_computador == "pedra":

                print("Escolha Jogador:", escolha_jogador, "Escolha Jogador:", escolha_computador)
                print("Você venceu!")

                return 1

            elif escolha_computador == "tesoura":

                print("Escolha Jogador:", escolha_jogador, "Escolha computado:", escolha_computador)
                print("O computador venceu!")

                return 0

        else: 

            if escolha_computador == "pedra":

                print("Escolha jogador:", escolha_jogador, "Escolha_computador:", escolha_computador)
                print("O computador venceu!")

                return 0

            elif escolha_computador == "papel":

                print("Escolha Jogador:", escolha_jogador, "Escolha computador:", escolha_computador)
                print("Você venceu!")

                return 1

    else:

        print("Temos um empate!")

        return 0

# escolhas = escolher() 

# print(escolhas["escolha_jogador"])
# print(escolhas["escolha_computador"])

escolhas = escolher()

verificar_vencedor(escolhas)