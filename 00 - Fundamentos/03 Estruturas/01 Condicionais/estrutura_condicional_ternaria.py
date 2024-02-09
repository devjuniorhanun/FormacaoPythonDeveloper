# Instanciando variávies
saldo = 2000
saque = 2500
# Verifica o status
status = "Sucesso" if saldo >= saque else "Falha"
# Imprimi o status
print(f"{status} ao realizar o saque!")