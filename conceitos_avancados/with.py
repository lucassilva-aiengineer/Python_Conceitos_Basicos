# Declaração with. 



# Abrindo e fechando um arquivo sem a palavra chave with. 

nome_arquivo = "exemplos_arquivos/arquivo_1.txt"

def testando_arquivo():

    file = open(nome_file, 'r')

    conteudo = file.read()

    print(conteudo)

def sem_utilizar_with():

    try: 
        file  = open(nome_file, 'r') 
        conteudo = file.read()
        print(conteudo)


    finally:

        # Terminamos o código e fechamos o arquivo. 
        file.close()


# Utilizando o with 

# O with acessa e fecha o arquivo automáticamente. 

def utilizando_with():

    with open(nome_arquivo, 'r') as arquivo: # Como o arquivo é uma variável local. 
        conteudo = arquivo.read()
        print(conteudo)


utilizando_with()