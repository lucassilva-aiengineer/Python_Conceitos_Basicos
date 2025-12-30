# Recursão. 
# A recursão se trata de uma função que chama a si mesma. 


# Recusão no cálculo fatorial. 

# O que é o fatorial de um número. 

# 3! = 3 x 2 x 1 = 6 
# 4! = 4 x 3 x 2 x 1 = 24 
# 5! = 5 x 4 x 3 x 2 x 1 = 120 


def fatorial(numero):

    if numero == 1: return 1
    return numero * fatorial(numero - 1)



print(fatorial(5))