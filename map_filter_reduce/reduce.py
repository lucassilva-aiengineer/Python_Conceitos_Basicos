# A função reduce é utilizada no calculo de valores de 
# saída. 

from functools import reduce 


clientes_receber = [
    ('Empresa 1', 2000.20),
    ('Empresa 2', 4000.5)
]

def funcao_a():

    total_receber = 0 
    for tupla in clientes_receber:

        total_receber += tupla[1]

    print(f"Total a receber: {total_receber:.2f}") 

# Utilizando a função reduce()

def teste_2():
    total_receber = reduce(lambda a, b : a[1] + b[1], clientes_receber) # Como a lista a receber é uma variável de escopo global ela é acessível na função. 

    print(total_receber)