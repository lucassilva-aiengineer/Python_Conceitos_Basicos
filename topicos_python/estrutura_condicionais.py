# Estrutura de condicionais 
# Estruturas de condicionais são estruturas que verificam se uma ou mais condições são cumpridas, 
# caso alguma destas condições seja cumprida, então a intrução contida no bloco de código que faz parte 
# do escopo desta condicional cumprida será executada. 


nome_string = "Mateus"

# Caso a condição seja cumprida este bloco de código, 
# esta instrução, será executado.

if nome_string == "Marcos":
    print("O nome da string é Marcos")

# Caso a condição anterior não seja cumprida então 
# esta condição será testada e se cumprida este bloco 
# de código será executado. 

elif nome_string == "Carlos":
    print("O nome da string é o nome Carlos.")


# Caso a condição anterior não seja cumprida esta 
# condição será testada, caso cumprida o bloco de
# código referente a ela será executado.  

elif nome_string == "Mateus":
    print("O nome da string é o nome Mateus.")

# Caso nenhuma das condições anteriores seja cumprida então 
# esta condição será inevitávelmente, executada. 
else: 

    print("Não sei qual é o nome que está na string...")

