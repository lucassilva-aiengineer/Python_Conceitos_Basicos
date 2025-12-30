# Excessões 
# As excessões  em python são uma maneira de identificar e tratar erros de 
# execução, contra medidas, caso um erro seja encontrado então retorne esta 
# opção. 

# try: 

#     print()
# except <Error1>:
#     print()
# except <Error2>:
#     pass 

# Podemos ter o else que é executado 
# caso nenhuma exceção ocorra ou seja encontrada. 

# else:


# finally: 

    # O bloco de código será executado independentemente de exceções serem 
    # encontradas ou não, será executado de qualquer maneira ao final do código, 
    # é interessante para fechar arquivos por exemplo. 


# Exemplo: 

def main():
    try:
        resultado = 2 / 0 

        print(resultado)

    except ZeroDivisionError as message:
        print(message)

        print("Não é possível dividir por zero!")
        print("Tente novamente...")

    else: 

        print("Nenhum erro encontrado!")
        print("Este bloco será executado caso nenhum ")


    finally: 

        print("Esta menssagem será executada independentemente de execeções serem encontradas ou não...")



# Escrevendo as nossas próprias mensagens de Error. 
def teste():
    try: 
        raise Exception('An error ')

    except Exception as error:
        print(error)



# Criando a nossa própria classe de ExceptionError.


class PessoaNaoEncontradaException(Exception): # Herdamos da classe exceção. 
    pass 


try:

    raise PessoaNaoEncontradaException()

except PessoaNaoEncontradaException as error:
    print(error)
    print("Pessoa não encontrada!")