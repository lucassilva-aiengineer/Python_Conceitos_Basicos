# Operadores Aritméticos 

print(1 + 1) # Operador de adição 
print(2 - 1) # Operador de subtração 
print(2 * 2) # Operador de multiplicação 
print(4 / 2) # Operador de divisão 
print(4 % 3) # Operador de divisão inteira, retorna apenas o resto desta divisão. 
print(5 // 2) # Flor division, arredonda o resultado da divisão para o inteiro mais próximo para baixo.  
print(4 ** 2) # Operador de potênciação, temos 4 elevado a 2. 

# O + pode ser utilizado como operador de concatenação. 
# string concatena apenas com string. 

frase = "Anda de bicicleta"
print("Ela " + frase + " desde os " + str(8) + " anos.")

idade = 10 
idade += 1 # idade = idade + 1

idade *= 2 # idade = idade * 2


print(idade)


# Operadores de comparação. 

# a = 1 
# b = 2 

# a == b # igual, variáveis que possuem o mesmo conteúdo 
# a != b # não igual 
# a > b # maior que 
# a >= b # maior que 
# a <= b # menor que 


# Operadores boleanos. 
# Bem ligado a lógica boleana. 

condicao_1 = True 
condicao_2 = False 

print(not condicao_1) # False, se a proposicao é verdadeira a negação dela é falsa, se a proposição é falsa a negação dela é verdadeira. 

# Conjunção, a conjunção é verdadeira apenas quando as duas proposições assumem ao mesmo tempo valores lógicos verdadeiros. 
print(condicao_1 and condicao_2) # numa condicional será verdadeira apenas se as duas condições forem cumpridas. 


# Disjunção, a disjunção é verdadeira quando ao menos uma das proposições assume valor lógico verdadeiro. 
print(condicao_1 or condicao_2) 

# O operador or, retorna o primeiro valor apenas se ele significar verdadeiro, caso contrário retorna o segundo valor 
print(False or True)
print(1 or 2)
print(0 or 1)
print(False or 1)

print()
print("Exemplos: ")

print(False or "Oi")
print("Oi" or "Boa tarde!")
print([] or False)
print(False or [])

# O operador and retornará o segundo valor apenas se o primeiro valor for verdadeiro.


print(0 and 1)
print(1 and 0)
print(False and "Oi")
print("Oi" and "Boa tarde!")
print([] and False)
print(False and [])


# Operadores Bit wise. 

# & Executa o AND binário 
# | Executa o OR binário 
# ^ Executa o XOR binário 
# ~ Executa a operação binária NOT 
# << operação de shift para esquerda 
# >> operação de shift para a direita  


# Operador in e o operador is. 

# is, o is se trata de um operador de comparação de objetos 
# ele verifica se aqueles objetos estão no mesmo endereço de memória. 
class Pessoa:

    def __init__(self, nome):
        self.__nome = nome


pessoa_1 = Pessoa("Lucas")
pessoa_2 = Pessoa("Lucas")

print(pessoa_1 is pessoa_2)

# in, o operador in se trata de um operador de membros, membership operator, 
# ele verifica se um certo valor faz ou não parte de uma estrutura de dados específica, como lista, dicionário, 
# cadeia de caracteres ou variável. 

nome_a = "Mateus"
print("Mateus" in nome_a) 
print("a" in nome_a)

lista = ["Lucas"]
print("Nome" in lista) 



# Operadores ternários. 
# Se trata de um estilo ou técnica de programação que nos permite construir estruturas de condicionais 
# menores, mais compactas. 

# Programando de forma tradicional. 

def e_adulto(idade):

    if idade > 18:

        return False
        # print("Você é um adulto.")

    else: 

        return True
        # print("Você ainda é um adolescente.")


def adulto(idade):

    return True if idade > 18 else False

print(adulto(10))