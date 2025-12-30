# Dicionarios 
# Dicionários são estruturas de dados ordenadas 

pessoa = {"nome": "Mateus", "idade": 20, "casado": True}

# Alterando valor pela chave. 

pessoa["nome"] = "Pedro"

print(pessoa['nome'])


# get()

print(pessoa.get("nome"))

# Podemo definir um valor padrão caso a chave não seja encontrada. 

print(pessoa.get("cidade", "Goiânia"))


# Removendo pares chave valor. 

print(pessoa.pop("nome"))

print(pessoa.get("nome"))

print("nome" in pessoa)



print(list(pessoa.keys()))

# valores. 
# Obtendo valores da lista 

print(pessoa.values())

# Obtendo uma lista com tuplas contendo o valor e a chave no dicionário. 

print(pessoa.items())

# Obtendo a quantidade de pares que o dicionário possui. 

print(len(pessoa))

# Adicionando um novo par de chave valor ao dicionário. 

pessoa["cidade"] = "São Paulo"

print(len(pessoa))

# Deletando uma chave do dicionário. 

del pessoa["idade"]

print(len(pessoa))

# Criando uma cópia do cicionário. 

copia_dicionario = pessoa.copy()

print(copia_dicionario)

