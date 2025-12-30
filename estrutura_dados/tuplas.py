# Tuplas são estruturas de dados em python que não podem ser alteradas, 
# são declaradas entre parentêses e também podem armazenar em si uma quantidade
# indeterminada de valores de diferentes tipos de dados e de outras estruturas. 


nomes = ("Mateus", "Pedro", "João")

# As tuplas são estururas de dados ordenadas. 

# Acessando itens das tuplas, por meio do índice. 

print(nomes[0])
print(nomes[-1])
# Acessado o índice de um termo específico. 
print(nomes.index("Pedro"))

# Função len()

print(len(nomes))

# Verificando a presença de um item. 

print("Mateus" in nomes)

# Fatiamento 

print(nomes[0:1])

# Ordenando tuplas. 
# sorted(), esta é uma função que ordena tuplas, que realmente cria uma nova lista, 
# com os itens ordenados da primeira. 

print(sorted(nomes))


# Criando novas tuplas por meio de tuplas existentes. 

nova_tupla = nomes + ("Raquel", "Rebeca")

print(nova_tupla)