# filter()

# A função filter itera uma lista buscando os elementos que são aprovados por um condição específicada. 

numeros_inteiros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def numeros_pares(numero):

    # Caso a divisão inteira do número pelo dois 
    # resulte em resto zero significa que aquele 
    # é um número inteiro. 

    return numero % 2 == 0

def main():
    lista_resultado = [numeros_pares(numero) for numero in numeros_inteiros]

    print(lista_resultado)




# Utilizando a função filter()

resultado_filter = list(filter(numeros_pares, numeros_inteiros))

print(resultado_filter)


# É uma função bem interessante para ciência de dados, filtrarmos condições cumpridas a cerca 
# de clientes de uma loja, por exemplo. 

numeros_filtrados = filter(lambda numero : numero % 2 == 0, numeros_inteiros)