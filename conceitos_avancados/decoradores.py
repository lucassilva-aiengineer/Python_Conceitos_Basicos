# Decoradores 

import time 
# Decoradores são uma forma de modificar o 
# comportamento interno de uma função. 


# O decorador é uma função que recebe outra 
# função como argumento e em si altera o comportamento 
# da mesma. 


def esperar_funcao(funcao):

    def run():
        print("Antes da função.")
        time.sleep(2)
        variavel = funcao()

        time.sleep(2)
        print("Depois da função.")

        return variavel

    return run


@esperar_funcao 
def saudacao():
    print("Olá!")

saudacao()