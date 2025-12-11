
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

almoco = random.choice(lista_comida)

print(almoco)

