# Strings 

# Strings são cadeias de caractes, são textos. 

# Podem ser assinalados, em aspas simples ou em aspas duplas. 
# e podem se atribuidas a variáveis ou a estruturas de dados, como listas 
# dicionários strings. 

def string():

    nome = "João"
    nome_a = 'João'

    print(nome)
    print(nome_a) 

# string() 

# Concatenando strings. 

def concatenando():

    nome = "Mateus"
    frase = "O nome dele é " + nome + ", e ele têm 20 anos."

    return frase 

# print(concatenando())  

# Juntando strings diferentes utilizando o operador += 

def juntando_strings():

    frase_1 = "Ele gosta de ir ao"
    substantivo = " cinema"

    frase_1 += substantivo

    idade = str(20)

    frase_1 += ". Ele tem " + idade 

    frase_1 += " anos."

    return frase_1

# print(juntando_strings())


# Podemos ter strings com várias linhas. 

# print("""
#     Um dois três...
#     Este projeto é um projeto sobre. 
# """)



# Métodos de strings 

nome = "Lucas"

print(nome.upper())
print("Lucas".upper())

print(nome.lower())

print("mAteuS sILvA".title())
# Organiza as palavras, para que a primeira letra de cada palavra seja maiúscula enquanto as outras minúsculas. 

print("MATeus".islower()) # Verifica se todas as letras das strings são minúsculas. 

print("mAtEUS".isupper())

print("Lucas".startswith('L'))

print("Lucas".endswith('s'))

print("Lucas gosta de programar em c".replace("programar em c", "programar em c e em python e em html e em dart e em outras linguagens."))
# Substitui uma parte da string por outra parte. 

texto = "Um, dia, dois, dias, três, dias"
lista_palavras = texto.split(',')
print(lista_palavras)
# O split quebra, ou melhor, separa uma string em uma lista de palavras seguindo um separador específicado. 

# print("t e x t o".strip(" "))


# O strip() limpa as estremidades das palavras, removendo espaços ou caracteres das estremidades. 
texto_1 = "email@gmail.com   "
novo_texto = texto_1.strip()
print(novo_texto)

# join(), o método join() pega uma lista de strings e as juntas em uma string apenas, em um único texto. 

palavras = ["O", "garoto", "joga", "bola", "nas", "manhas", "de", "quinta"]
nova_frase = ",".join(palavras)
nova_frase_1 = "1".join(palavras)

print(nova_frase)
print(nova_frase_1)

# find(), o método find encontra a posição, índice de uma substring()

texto_2 = "O garoto gosta de correr"
print(texto_2.find("gosta"))


# Os métodos de string não alteram a string original. 

nome = "JOão"
nome_alterado = nome.title()

# Ou seja o nome original não foi alterado. 

print(f"Nome alterado: {nome_alterado}")
print(f"Nome original: {nome}")

print(nome.lower())
print(nome)

# A função len(), nos retorna o comprimento de nossa string ou lista, 
# Nos retorna a quantidade de posições que a nossa estrutura de dados possui. 

tamanho = len(nome)
print(nome)

# Utilizando o operador in para verificar a presença de uma parte de string em uma string maior 
print("Jo" in nome)

# Escaping caracter
print("\"A terra é azul\" - Autor da frase")


nome = "'Lucas'"

print(nome)


print("Hoje o sol \n está brilhando")

# A barra invertida omite a segunda.
print("A criança gosta de comer chocolate\\")


# Fatiamento 
# Acessando partes de strings por meio de seus índices. 

nome_2 = "Mateus"
# Em programacao contamos apartir do zero.
print(nome_2[0])
print(nome_2[2])

# Imprimindo o último item da string. 
print(nome_2[-1]) 

# Fatiamento. 
# Imprimindo partes da string, partindo de um índice e indo até outro índice 
# específicado menos 1. 

print(nome_2[0: 2]) # índice 2 - 1, índice 1. 
print(nome_2[:3]) # Por padão inícia no índice 0. 
print(nome_2[:]) # Percorre do índice zero ao final. 
print(nome_2[2:]) # quando não específicado percorre até o último índice. 

