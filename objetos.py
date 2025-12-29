# Objetos 
# Em python muitas coisas são objetos, objetos são instâncias 
# de classes, são classes que são executadas com dados que preenchem 
# os seus próprios atributos, objetos em python são uma tentativa por meio 
# do código representar coisas, objetos do mundo real. 


age = 8 

# Atributos
print(age.real)
print(age.imag)


# Métodos 
print(age.bit_length()) # A quantidade de bits utilizadas para armazenar este número. 


# Um objeto lista.
itens = [1, 2]
itens.append(4)

# Este método remove o último item da lista, e exibe o valor que foi removido.
itens.pop()



# A função global id()
# Esta função é utilizada para encontrarmos a localização dos objetos na memória do computador, 
# nós enconramos o endereço de memória da quele objeto. 

print(id(age)) 
