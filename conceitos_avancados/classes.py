# Classes 
# Classes são como o modelo geral de um objeto, desenhado no algoritmo 
# pelo meio da qual poderão ser criados objetos que seguirão o modelo 
# mas possuindo os sus próprios dados. 

class Pessoa: 

    def __init__(self, nome, idade):
        self.nome = nome 
        self.__idade = idade 
        self.__posicao_atual = 0

    @property 
    def posicao_atual(self):
        return self.__posicao_atual

    def andar(self):
        self.__posicao_atual += 1

        return ("posição atual: ", self.__posicao_atual)



class Funcionario(Pessoa):

    def correr(self):
        print("Estou correndo...")

pessoa_1 = Pessoa("Nome", 20)
pessoa_1.andar()

print(type(pessoa_1))

print(pessoa_1.nome)

print(pessoa_1.andar())

funcionario = Funcionario("Funcionario", 30)

print(funcionario.nome)

print(funcionario.andar())