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


