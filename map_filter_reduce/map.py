# map() - filter() - reduce()
# São funções gloabais especiais em python. 

# map()

numeros = [1, 2, 3]

def dobrar_numero(numero):
    return numero * 2 

# A função map(), funciona iterando uma função específica para cada termo em uma lista, 
# em um iterável. 

# O mesmo código com uma função lambda. 

dobrar_numero_a = lambda numero : numero * 2 

numero_dobrados = map(dobrar_numero_a, numeros)

# Passando a função com argumento. 

numeros_dobrados_a = map(lambda numero : numero * 2, numeros)
print(list(numero_dobrados))

