# List compression. 
# List compression se trata de uma maneira de criarmos listas de forma mais fácil. 
# Com apenas uma linha de código. 

import math


numeros_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_elevados_2 = [numero ** 2 for numero in numeros_a]

print(numeros_elevados_2)


elevar_numero = lambda numero, expoente : numero ** expoente


numeros_elevados_5 = [elevar_numero(numero, 5) for numero in range(0, 10)]

print("Números elevados a 5: ")

def mostrando_resultado():
    indice = 0
    for numero in numeros_elevados_5:
        print(f"{indice} ** 5 = {numero}")

        indice += 1

numeros = [a for a in range(0, 100)]
print(numeros)

