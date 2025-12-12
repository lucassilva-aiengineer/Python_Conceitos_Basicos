
# Variável 
# Uma variável é como um espaço alocado na memória que pode armazenar qualquer tipo 
# de dados, desde um int (inteiro) até um bool, valor boleano, valor lógico (True ou False) ou string, uma cadeia 
# de caracteres, ou simplesmente texto. Quando você chama uma variável pelo nome na verdade você chama o valor que 
# está atribuido a aquele espaço de memória. 


# opcao_jogador = "Pedra"
# opcao_computador = "Papel"


# Funções 
# Uma função se trata de um bloco de código que pode ou não receber argumentos, chamados de parâmetros enquanto 
# se escreve o algortimo, e é executado apenas quando é chamado, ou seja, se trata de um bloco reutilizável de 
# código. 

def opcao():

    opcao_jogador = "Pedra"

    return opcao_jogador 

# Nós temos então que quando a função opcao for chamada, esta funcao "valerá", retornará
# a escolha do jogador 

def funcao_a(argumento):

    # print(opcao())

    if argumento == 1:

        # A função em uma váriavel
        escolha_jogador = opcao()

        print("Opção:", escolha_jogador)

    else: 

        # Executando a função diretamente na função print().
        print("Opção 2: " + opcao())


# funcao_a(2)
# funcao_a(1)

# Indentação. 
# Indentação se trata do recuo ou espaço que antecede o código e serve para definir o escopo daquele bloco de código 
# ou seja, o escopo da função, da estrutura de condicional, o escopo do laço de repetição. 



def saudacao():

    return "Oi"

# print(saudacao())

# resposta = saudacao()

# print(resposta)



# Dicionários 
# Dicionários se tratam de uma estrutura de dados python onde temos a possibilidade 
# de armazenar uma quantidade indefinida de conjuntos de pares chave valor, onde um valor 
# que pode ser de qualquer tipo de dados como bool (True ou False), float (número decimal), 
# int (inteiro), str (string) ou mesmo outras estruturas de dados (listas, conjuntos, tuplas) armazenando dados, que podem 
# ser de diferentes tipos.  

# dicionario = {"Nome": "Lucas", "Cor": "Azul"}  

cor = "Verde"


# Os valore podem ser atribuidos por meio de variáveis, ou objetos. 

dicionario = {"Nome": "Lucas", "Cor": cor}


# Acessando valores em um dicionário por meio de chave. 

# Definindo um argumento padrão, caso nenhum seja passado.
def imprimir(argumento= "Nome"):
    dicionario_nome = dicionario[argumento]

    print(dicionario_nome)

# imprimir("Cor")




# Função input() - Entradas de Usuário. 

# A função input(), se trata de uma função que permite ao usuário fornecer uma entrada de 
# dados que será armazenada na memporia, e, geralmente atribuida a uma variável e pode ser 
# manipulada pelo algoritmo, é basivamente uma entrada ao usuário, uma forma de permitir que 
# o usuário forneça uma entrada ao código, geralmente pormeio do console, também chamado de terminal
# ou até prompt de comando. 



# Bíbliotecas 
# Bíbliotecas são algo muito interessante dentro do mundo de programação python, pois se trata de uma 
# forma de você não necessitar de criar tudo do zero, mas sim importar alguma funcionalidades, funções, 
# variáveis, classes e dados, que outros programadores já desenvolveram préviamente. 


# para utilizarmos ás bibliotecas nós podemos utilizar a palavra chave import que irá nos 
# importar, ou trazer um página de arquivo de código que contém algumas funções, classes,
# variáveis e dados específicos que foram desenvidos por algum programador. 

# poderiamos também utilizar a palavra chave from, que nos permite de dentro de um arquivo 
# ou de uma pasta de arquivos acessar-mos um arquivo ou de um arquivo a uma função específico. 


# importando uma bíblioteca de geração de valores aleatórios. 

import random 

# Listas - Outra estrutura de dados. 
# As listas são uma estrutura de dados em python que nos permite armazenar um quantidade indefinida 
# de termos de diferentes tipos de dados, como: boleano, float, int, str, caracter; ao mesmo tempo, e ou 
# vários outros tipos de estruturas de dados em si. Podemos acessar estes valores armazenados por meio 
# de seus índices. 


lista_comida = ["Pizza", "Bolo", "Chocolate"]

# utilizando a função choice() da biblioteca random para escolher um termo aleatóriamente na lista. 

# almoco = random.choice(lista_comida)

# print(almoco)


# Argumentos 
# Os argumentos são informações que as funções podem receber e utilizar em seu interior.
# nas funções def, que são criadas utilizando a palavra chave def, os argumentos, também chamados parâmetros 
# no algoritmo da função, são indicados quando utilizamos a função no interior de parênteses.  


# Exemplo: 

def saudacao(tipo_saudacao):

    return tipo_saudacao 

print(saudacao("Olá!"))


def saudacao_nome(tipo_saudacao, nome):

    return str(tipo_saudacao) + " " + str(nome)


saudacao_a = saudacao_nome("Bom dia!", "Pedro")

# print(saudacao_a)



# Estruturas de condicionais. 

# As estruturas de condicionais são estruturas que nós utilizamos 
# para executar ou não um bloco de código caso uma condição seja cumprida. 

# if, utilizamos o if para verificarmos se uma codição está sendo cumprida, 
# caso esta condição estaja sendo cumprida nós executamos um bloco de código específicado. 

# Ex:

def verificando_clima(): 

    chuva = True

    if chuva == True: 
        print("Está chovendo!")


# else, nós utilizamos o else para verificarmos se ao menos uma das condições anteriores ocorreram 
# caso nenhuma das condições anteriores tenha sido cumprida será executada a instrução definida no 
# else. 


def verificando_temperatura():

    temperatura = 15
    if temperatura >= 20:
        print("Está calor!")


    else: 
        print("Está Frio!")


# elif, a palavra-chave se traduz em algo que verifica se a condição anterior foi cumprida 
# caso contrário, a condição elif é testada, se não a próxima condição elif é testada e assim 
# sucessivamente. A condição if têm origem da junção da palavra-chave if com a palavra-chave else. 

# Ex. 

def verificando_numero(numero):


    if numero < 3: 

        print("Este número é menor que três!")

    elif numero < 5:

        print("Este número é menor que cinco!")

    elif numero < 7: 

        print("Este número é menor que sete.")

    else: 

        print("Este número é maior ou igual a sete!")


# verificando_numero(6)

a = 1 # Neste caso o igual se trata de um operador de atribuição. 

a == 2 # Neste caso se verifica se o valor de a é igual ao valor de b. 



# Operadores de comparação: 

# >= maior ou igual 
# <= menor ou igual 
# == igual 
# != não igual  


# Concatenação 
# Concatenar se trata de imprimir strings com números ou com variáveis. 
# Strings se concaetem apenas com strings. 

# Algumas formas de concatenação 

# com o sinal de mais:
# idade = 10 
# print("A idade dele é: " + str(idade) + " " + "anos.")

# # com vírgula: 
# print("A idade dele é:", idade, "anos.")

# # f - string 

# print(f"A idade dele é: {idade} anos.")