# Tipo de dados numéricos. 


# Números complexos. 
# São números formados da adição de uma parte imáginaria a uma parte inteira. 

numero_1 = 2 + 3j 
numero_2 = complex(2, 3)

numero_complexo_1 = numero_1.real 

print(numero_complexo_1)

print(numero_1.real, numero_2.imag)


# A função gloabal abs(). 
# Esta função gera o número absoluto do número, também conhecida como módulo. 
# Se o valor está negativo retorna o número positivo, o oposto, caso seja um número, positivo, 
# retorna o mesmo valor. 

numero = -5 
numero_absoluto = abs(numero)

print(numero_absoluto)

# A função global round(), esta função retorna o número inteiro mais próximo, 
# preferencialmente, na metade do caminho, retornando para cima. 

print(round(5.49))

# Podemos adicionar argumentos que irão dizer qual o nível de incrementação, se a nível decimal ou centésimal. 

print(round(5.49, 1))


