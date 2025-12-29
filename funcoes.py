# Funções
# São estruturas de código reutilisáveis, que são executadas 
# quando chamadas. 

def saudacao(nome= "Usuário", idade= 20):
    print("Olá!", nome, "a sua idade é",
    idade, "anos.")

saudacao("Lucas")
saudacao("Mateus", 10)

# Escopos de uma variável 

def mudar_valor(variavel, variavel_2):

    variavel["nome"] = "João"

    variavel_2 = 2

    # O valor que alteramos no interior da função 
    # não altera nada no exterior da função, isto vale 
    # pare objetos imutáveis, como ints, floats, strings, etc. 

    # Estruturas de dados mutáveis de escopo gloabal podem ser alteradas por funções 
    # de escopo local. 



dicionario = {"nome" : "Mateus"}
valor = 10

mudar_valor(dicionario, valor)

print(dicionario)
print(valor)



# Declaração de retorno 
# As declarações de retorno fazem com que a função retorne um valor, 
# quando as declarações de retorno são acionadas a função para imediatamente. 

def saudacao_a(nome):

    if not nome:
        return 

    print("Ola" + nome + "!")

    return 10, nome, "Mateus"

# saudacao_a("Mateus")
# saudacao_a("João")

# print(saudacao_a("Marcos"))



# Escopos de variáveis. 

idade = 10 # Variáveis globais 

def teste():

    idade_a = 15 # Variável local
    print(idade) # É visível no interior da função. 


# print(idade)

# print(idade_a) # Não é visível fora da função.
# teste()


# Aninhamento de funções. 

def falar(frase):

    def dizer(palavra):
        print(palavra)

    palavras = frase.split(' ')
    for palavra in palavras:

        dizer(palavra)

frase_a = "Eu gosto de ler livros sobre gerenciamento de projetos"
falar(frase_a)