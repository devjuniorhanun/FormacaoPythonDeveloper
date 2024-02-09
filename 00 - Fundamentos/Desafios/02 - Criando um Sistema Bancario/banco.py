# Criando um Menu
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# Instancia as variáves
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2
# Cria um loop infinito
while True:
    # Instancia a variável de opção de operções bancarias
    opcao = input(menu)

    # Verifica se a opção e Deposito
    if opcao == "d":
      # Recebe o valor a ser depositado
      valor = float(input("Informe o valor do depósito: "))
      # Verifica se o deposito e maior que zero
      if valor > 0:
          # Incrementa o saldo
          saldo += valor
          # Incrementa o Extrato
          extrato += f'Deposito: R$ {valor: .2f}\n'
      # Ser o valor fo negativo    
      else:
          # Imprime
          print("Operação falhou! O valor informado é inválido. Tente novamente!")

    # Verifica se a opção e Saque
    if opcao == 's':

        # Recebe o valor a ser Sacado
        valor = float(input("Informe o valor do saque: "))
        # verifica se saque e maior que saldo
        excedeu_saldo = valor > saldo
        
        # verifica se saque e maior que limite
        excedeu_limite = valor > limite
        
        # verifica a quantidade de saques
        excedeu_saques = numero_saques >= LIMITE_SAQUES
      
        # Imprime
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo sufuciente.")
        
        # Imprime
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        # Imprime
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")
        # Imprime
        elif valor > 0:
            saldo -= valor

            extrato += f'Saque: R$ {valor: .2f}\n'

            numero_saques += 1

        # Imprime
        else: 
            print("Operação falhou! O valor informado é inválido.")

    # Verifica se a opção Extato
    if opcao == "e":

        print("\n=============EXTRATO==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================")        

    # Finaliza o Sistema
    elif opcao =="q":
          break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")