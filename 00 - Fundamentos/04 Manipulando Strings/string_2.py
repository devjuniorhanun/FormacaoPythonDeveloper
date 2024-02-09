# Instanciando variávies
nome = "Nome"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435
dados = {"nome": "Nome", "idade": 28}
# Imprimi Nome: Nome Idade: 28
print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))
# Imprimi Nome: Nome Idade: 28
print("Nome: {1} Idade: {0}".format(idade, nome))
# Imprimi Nome: Nome Idade: 28 Nome: Nome Nome
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
# Imprimi Nome: Nome Idade: 28
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# Imprimi Nome: Nome Idade: 28 Nome Nome 28
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
# Imprimi Nome: Nome Idade: 28
print("Nome: {nome} Idade: {idade}".format(**dados))
# Imprimi Nome: Nome Idade: 28
print(f"Nome: {nome} Idade: {idade}")
# Imprimi Nome: Nome Idade: 28 Saldo: 45.44
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# Imprimi Nome: Nome Idade: 28 Saldo:       45.4
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")