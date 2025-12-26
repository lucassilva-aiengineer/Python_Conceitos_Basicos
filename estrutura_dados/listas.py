# Listas 
# As listas são uma estrutura de dados em python, uma das mais utilizadas, 
# talvez a mais utilizada na linguagem python, elas adimitem armazenar uma quantidade 
# indeterminada de itens, de diferentes tipos de dados, de quaisquer tipo de dados da
# liguagem python, seja booleano, NoneType, float, números decimais, ints, números inteiros. 

lista_1 = ["Nome", True, False, None, 1, 100, 0.5]

# print(type(None))
# variavel = None 

# verificando_tipo = isinstance(variavel, NoneType)

# print(isinstance(10, int) == True)


# print(type(None))



# Utilizando o operador in para verificar a presença de um elemento, item, na lista. 

def operador_in():
    print("Nome" in lista_1)

    if 100 in lista_1:
        print("100 está na lista 1")


# Acessando itens da lista pelos seus índices. 

item_1 = lista_1[0]
print(item_1)

# Acessando o último item da lista 
# As listas assim como as strings são cíclicas. 
print(lista_1[-1])

print(lista_1[-2])


# Atualizando item na lista pelo índice. 

lista_1[2] = True 
print(lista_1)
print(lista_1[2])


# Fatiamento, imprimindo seções da lista. 

parte_a = lista_1[1:4] # Imprimindo do item de índice 1 até ao índice 4 - 1. 
print(parte_a)


lista_a = lista_1[:1] # Imprimindo a partir do índice 0
print(lista_a)


tamanho_lista = len(lista_1)
print(tamanho_lista)

# append()
# O método append(), é uma função utilizada para adicionar elementos nas listas. 

lista_1.append("Ele gosta de chocolate.")
print(lista_1)

# extend()
# O método extend() é uma outra forma de adicionarmos elementos a lista, uma forma de juntarmos os elementos 
# de uma lista aos elementos de outra lista. 

# Juntando uma lista a outra. 
lista_b = ["Azul", True, None, 1, 0.100, "A"]
lista_1.extend(lista_b)

print(lista_1)

# Utilizador o operador += . 
# Nós também podemos utilizar o operador de mais igual para acrecentar partes de lista a uma outra lista, para juntarmos listas, 
# de uma forma parecida com o método extend. 

lista_1 += ["novo_texto", True, {}, (0, 1)] # É o mesmo que dizer esta lista anterior mais esta outra lista aqui, lista_a = lista_a + lista_2
print(lista_1)


# remove(), Nós utilizamos o método remove() para remover elementos da lista. 


