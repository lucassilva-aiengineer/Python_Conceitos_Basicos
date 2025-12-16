# Variáveis  

# Variávieis em python são um espaço alocado na ao qual nós atribuimos valores que podem ser qualquer tipo 
# de dados ou até mesmo de estruturas de dados, e quando chamamos uma váriavel, na verdade não estamos chamando a 
# variável mais o valor a ela atribuido. 

# Podemos utilizar quaisquer tipo de escrita para declararmos uma variável, execeto números, palavras chaves do python e 
# caracteres de pontuação. 
# Existem vários tipos de convenções de escritas para a declaração de variável, mas, a mais comum em python é a snake case 
# onde escrevemos com letras minusculas e as separacoes entre as palavras com um sublinhado, no caso o underscore, também 
# chamado de underline. 


# nome = "Lucas"
# idade = 10 
# print(nome)
# print(idade)
# print(idade + 10)


# Uma curiosidade podemos separar as declarações com pontos em vírgula 

nome = "Lucas"; print(nome)  # Podemos 

# Declarações. 
# Quando nós atribuimos valores a uma variável, nós temos uma declaração. 


# Comentários. 
# Comentários, são uma forma de escrever coisas que o compilador e o interpretador vão ignorar como código, 
# são anotações, precedidas pelo símbolo de jogo da velha #, que utilizamos para escrevermos informações sobre o código, 
# para nós mesmos ou para outras pessoas. 

comentario = "O nome dele é Marcos."
print(comentario)  # Também podemos comentar desta maneira. 



# Indetação. 
# Indentação se trata de um espaço em branco, um recuo, que precede o código e serve para definir qual o escopo daquele bloco de código. 

def verificar_nome():
    if "Marcos" in comentario: 
        print("O nome Marcos está na string!")  
    else:
        print("O nome Marcos não faz parte da string!")


# Exemplo de indentação ruim. 

# nome = "José"
#     print(nome)

# Veirificando o tipo de dados 

tipo = type(comentario)
print(tipo)

# Verificando se é um tipo de dados específico. 

print(type(comentario) == str)
print(type(comentario) == int)
print(type(comentario) == float)


# Verificando se a variável comentário é um objeto de uma determinda classe. 

print(isinstance(comentario, str))


# int() 
# Inteiros. 

idade = 10 
print(type(idade))
print(isinstance(idade, int))


# Podemos modificar um tipo de dados para outro tipo de dados. 

# passando um inteiro para float()
numero = float(2)
print(type(numero))


# Passando um inteiro para string. 
numero_a = "20"
print(type(numero_a))

idade_a = int("20")
print(isinstance(idade_a, int))