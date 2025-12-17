
# Enuns,
# Enums, são número legíveis associados a um valor constante. 

from enum import Enum 


class Estado(Enum): # Herda a classe Enum, por isso, herda atributos e métodos desta classe. 

    INATIVO = 0
    ATIVO = 1


# Retornamos o estado. 
print(Estado.ATIVO)

# Retornamos o valor associado ao termo ao termo "Ativo"
print(Estado.ATIVO.value)

print(Estado.INATIVO.value)

# É uma forma de criarmos constantes em python. 

print(Estado['ATIVO'])
print(Estado['ATIVO'].value)

# Podemos imprimir uma lista de estado. 
print(list(Estado))

# Contando as possíbilidades de estado. 

print(len(Estado))
