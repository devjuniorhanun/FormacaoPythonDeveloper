# Instancia uma variável
opcao = -1

# Cria um Loop While ate ser digitado 0 para sair
while opcao != 0:
    # Recebe o valor digitado no terminal
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    # Verifica se foi digitado 1
    if opcao == 1:
        # Imprimi
        print("Sacando...")
    # Verifica se foi digitado 1
    elif opcao == 2:
        # Imprimi
        print("Exibindo o extrato...")
# Final da Execução 
else:
    # Imprimi
    print("Obrigado por usar nosso sistema bancário, até logo!")