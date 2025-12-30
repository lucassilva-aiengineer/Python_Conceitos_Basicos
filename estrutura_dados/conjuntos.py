# Sets. 
# Os conjuntos, são estruturas de dados mutáveis, porém não ordenadas. 
# que podem receber vários tipos de dados diferentes. 

conjunto_1 = {"Mateus", "João", "Pedro", "Levi", "Roberto"}

# Podemos realizar operações com conjuntos. 

conjunto_2 = {"Roberto"}

intercecao = conjunto_1 & conjunto_2

# O que esá no conjunto a e no conjunto b

print(intercecao)

# União

# O que há no conjunto ou no conjunto b 
uniao = conjunto_1 | conjunto_2
print(uniao)


# Diferença de conjuntos 

diferenca = conjunto_1 - conjunto_2
print(diferenca)

# Algumas operacoes 

maior = conjunto_1 > conjunto_2
print(maior)

menor = conjunto_1 < conjunto_2
print(menor)

print(list(conjunto_1))


print("Mateus" in conjunto_1)