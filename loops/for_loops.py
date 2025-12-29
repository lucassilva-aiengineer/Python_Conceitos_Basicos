
# numeros = [1, 2, 3, 4, 5, 6]

# for numero in numeros:

#     print(numero)



# numero = range(0, 10)
# for item in range(15):
#     print(item)

# print(numero)

numeros = [1, 2, 3, 4, 5]

for index, numero in enumerate(numeros):

    print("numero: ", numero)
    print("index: ", index)


lista_nome = ["João", "Raquel", "Mateus"]

# A função enumerate nos retorna uma lista de tuplas 
# onde o primeiro valor da tupla é o índice do termo na 
# lista e o segundo é o próprio termo. 

print(list(enumerate(lista_nome)))


# break & continue.


numeros_a = [1, 2, 3, 4, 5]

for numero in numeros_a: 

    if numero == 2:

        # O continue caso o número dois seja encontrado 
        # inpede que o bloco de código, no caso o print(), 
        # seja executado. 

        # nesta iteração ele pulou e deixou de executar o bloco de código. 
        continue 

    print(numero)



for numero in numeros_a: 

    if numero == 2:

        print("Numero 2 encontrado!")
        break 

    # Caso o número 2 seja encontrado o laço de repetição é interrompido. 
    print(numero)