# Operadores overloading. 
# operadores overloading são uma forma interessante de utilizando métodos dunder, double underscore, 
# permitir a comparação de objetos. 


class Pessoa:

    def __init__(self, nome, idade):

        self.__name = name 
        self.__idade = idade 

    @property 
    def idade(self):
        return self.__idade

    def __gt__(self, outro_objeto_pessoa):

        return True if self.__idade > outro_objeto_pessoa.idade  else False 

    def __lt__(self, outro_objeto_pessoa):

        return True if self.__idade < outro_objeto_pessoa.idade else False




pessoa_1 = ("Mateus", 10)
pessoa_2 = ("Levi", 12)

print(pessoa_1 > pessoa_2)
print(pessoa_1 < pessoa_2)


# Mais exemplos de métodos dunder 

#  +  __add__(self, other)       Adição
#  -  __sub__(self, other)       Subtração
#  *  __mul__(self, other)       Multiplicação 
#  /  __truediv__(self, other)   Divisão Real
#  // __floordiv__(self, other)  Divisão Inteira
#  ** __pow__(self, other)       Potência
#  %  __mod__(self, other)       Módulo (resto)