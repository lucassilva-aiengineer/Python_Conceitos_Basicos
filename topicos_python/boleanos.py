# Boleanos. 
# Os boleanos são um tipo de dados voltado a representação de valores boleanos, muito ligados, ou totalmente ligados 
# a lógica boleana. Eles servem para representar dois valores ou verdadeiro True ou falso False. 


# Todos os números, exceto o 0, representam verdadeiro. 
# A strings são falsas apenas quando a string estiver vazia. 
choveu = True 

def boleano(variavel):

    if variavel:
        print("Sim, choveu!")

    else: 
        print("Não, choveu!")


boleano(choveu)

def string():

    texto = ""

    # Só irá acontecer se o texto representar verdadeiro.  
    # Este bloco de código será executado apenas se a variável texto estiver representando algo verdadeiro, 
    # uma string que não é vazia, ou um número que não seja zero, ou uma estrutura de dados como lista, dicionário 
    # ou tupla que não esteja vazia. 
    if texto: 
        print("A string representa falso")
        print("false.")

    else: 
        print("Não.")

string()

print(type(choveu)) 
print(isinstance(choveu, bool))

print(type(choveu) == str)
print(type(choveu) == bool)

# A função global any(), é uma função que retorna verdadeiro caso um dos valores de uma lista não seja verdadeiro, 
# caso um dos valores seja verdadeiro a função any() retornará verdadeiro. 

livro_1 = False
livro_2 = True

livros_lidos = any([livro_1, livro_2])
print(livros_lidos)


# A função global all() retorna True, caso todos os valores da lista sejam verdadeiros. 

livros = all([livro_1, livro_2])
print(livros)

