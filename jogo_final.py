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

                print("Escolha Jogador:", escolha_jogador, "Escolha computador:", escolha_computador)
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

# escolhas = escolher()

# verificar_vencedor(escolhas)

def vencedor_partida(pontuacao_a):

    pontos_jogador = pontuacao_a["pontos_jogador"]
    pontos_computador = pontuacao_a["pontos_computador"]


    if pontos_jogador == pontos_computador:

        print("Você e o computador empataram!")
        print(f"""Pontos Jogador: {pontos_jogador}
Pontos Computador: {pontos_computador}""") 

    elif pontos_jogador > pontos_computador:

        print("Você venceu esta partida!")
        print(f"""Pontos Jogador: {pontos_jogador} 
Pontos Computador: {pontos_computador}""")

    else:
        print("O computador venceu esta partida!")
        print(f"""Pontos Jogador: {pontos_jogador}
Pontos Computador: {pontos_computador}""")

def main():

    pontos_jogador = 0 
    pontos_computador = 0 


    pontuacao = {"pontos_jogador": pontos_jogador, "pontos_computador": pontos_computador}
    print("Bem vindo ao jogo \"Pedra, Papel,Tesoura\" !")

    while True:

        print("Para jogar mais uma vez digite 1.")
        print("Para sair do jogo digite 2.")

        opcao = int(input("Digite a sua opção: "))

        if opcao == 1: 

            escolha = escolher()
            pontos = verificar_vencedor(escolha)

            if pontos == 1:
                pontos_jogador += 1 

            else: 
                pontos_computador += 1

        elif opcao == 2:

            print("Encerrando Partida...")
            time.sleep(2)

            vencedor_partida(pontuacao)

            break

        else:

            print("Opção não esperada.")
            time.sleep(2)

            print("Tentando novamente...")
            time.sleep(2)


try: 

    main()

except ValueError as msg:
    print(msg)
    print("Opção inválida!")
    time.sleep(2)
    print("A sua opção deve utilizar o tipo de dados texto.")  
    print("") 
    time.sleep(2)
    print("Tentando novamente...")
    print("...")
    time.sleep(2)

    main()