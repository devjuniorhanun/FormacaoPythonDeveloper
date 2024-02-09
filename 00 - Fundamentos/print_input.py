# Variável que recebe um valor pelo terminal
nome = input("Informe o seu nome: ")
# Variável que recebe um valor pelo terminal
idade = input("Informe a sua idade: ")
# Imprimi as variávies
print(nome, idade)
# Coloca ... no final da linha com uma quebra de linha
print(nome, idade, end="...\n")
# Modifica espaço em #, e coloca ... no final da linha com uma quebra de linha
print(nome, idade, sep="#", end="...\n")
# Modifica espaço em #
print(nome, idade, sep="#")