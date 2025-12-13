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