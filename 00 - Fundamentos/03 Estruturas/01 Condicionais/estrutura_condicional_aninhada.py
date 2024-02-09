# Instanciando variávies
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450
# Verifia se uma conta normal
if conta_normal:

    # Verifica se saldo e maior que saque
    if saldo >= saque:
        # Imprimi
        print("Saque realizado com sucesso!")
    # Verfica se saque e menor
    elif saque <= (saldo + cheque_especial):
        # Imprimi
        print("Saque realizado com uso do cheque especial!")
    # Se o saque for maior que o saldo em conta
    else:
        # Imprimi
        print("Não foi possivel realizar o saque, saldo insuficiente!")
# Verifica se uma conta universitaria
elif conta_universitaria:

    # Verifica o saldo
    if saldo >= saque:
        # Imprimi
        print("Saque realizado com sucesso!")
    # Se não tiver saldo
    else:
        # Imprimi
        print("Saldo insuficiente!")
# Verifica se uma conta especial
elif conta_especial:
    # Imprimi
    print("Conta especial selecionada!")
# Se não encontrou o tipo de conta
else:
    # Imprimi
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")