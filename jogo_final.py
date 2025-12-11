import time
def escolher():

    print("Escolha a sua opção (Pedra, papel ou tesoura).")

    time.sleep(2)
    escolha_jogador = input("Indique a sua opção: ")

    escolha_computador = "Papel"

    # Vamos armazenar as nossas escolhas em um dicionario alocado na memória, atribuido a uma variáve. 

    escolhas = {"escolha_jogador": escolha_jogador ,"escolha_computador": escolha_computador}

    return escolhas


escolhas = escolher()

print(escolhas["escolha_jogador"])
print(escolhas["escolha_computador"])