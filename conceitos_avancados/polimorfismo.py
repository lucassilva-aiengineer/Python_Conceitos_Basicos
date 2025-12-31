# Polimorfismo 
# Polimorfismo se trata de um conceito que vem de programação orientada a objetos que 
# se resume em implementarmos os mesmos métodos de diferentes formas. 


class Funcionario:

    def liberar_acesso(self):
        print("Funcionario liberando acesso!")



class Gerente:

    def liberar_acesso(self):
        print("Gerente liberando acesso!")



funcionario = Funcionario()
gerente = Gerente()

funcionario.liberar_acesso()
gerente.liberar_acesso()