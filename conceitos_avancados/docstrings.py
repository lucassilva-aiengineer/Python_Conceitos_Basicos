# Docstrings 



""" Este arquivo 
    testa as Docstrings.


"""


def aumentar_valor(numero):

    """ Esta função aumenta o valor de um número """

    return numero + 1




class Pessoa:

    """Essa é a classe pessoa"""
    def __init__(self, nome, telefone, endereco):

        self.__nome = nome 
        self.__idade = idade
        self.__localizacao = 0

    def caminhar(self):
        """Este é o metodo de caminhada, ele atualiza 
        a posição atual da pessoa. """

        self.__localizacao += 1
        print("Estou caminhando ...")



# Acessando as Docstrings por meio da função global help()

print(help(Pessoa))