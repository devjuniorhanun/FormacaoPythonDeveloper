# Cria um Loop While, ate que seja digita 10 para sair
while True:
    # Imprimi
    numero = int(input("Informe um número: "))

    # Verifica se o numero e igual a 10
    if numero == 10:
        # Finaliza a aplicação
        break

    # Verfica se numero e par
    if numero % 2 == 0:
        # Continue a aplicação
        continue

    # Imprimi
    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")