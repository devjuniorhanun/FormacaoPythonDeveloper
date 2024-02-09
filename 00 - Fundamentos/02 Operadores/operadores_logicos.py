# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True
# Imprime true
print(True and True and True)
# Imprime false
print(True and False and True)
# Imprime false
print(False and False and False)
# Imprimi true
print(True or True or True)
# Imprime false
print(True or False or False)
# Imprime true
print(False or False or False)

# Instanciando variáveis
saldo = 1000
saque = 250
limite = 200
conta_especial = True


# Retorna true
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

# Retorna true
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
# Retorna true
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)