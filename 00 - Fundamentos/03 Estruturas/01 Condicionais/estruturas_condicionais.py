# Instancia constantes
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
# Idade receber o que o usuario digitou
idade = int(input("Informe sua idade: "))
# Verifica se idade e maior ou igual a idade
if idade >= MAIOR_IDADE:
    # Imprimi
    print("Maior de idade, pode tirar a CHN.")
# Verifica se idade e menor 
if idade < MAIOR_IDADE:
    # Imprimi
    print("Ainda não pode tirar a CNH.")

# Verifica se a idade e maior ou igual
if idade >= MAIOR_IDADE:
    # Imprimi
    print("Maior de idade, pode tirar a CHN.")
else:
    # Imprimi
    print("Ainda não pode tirar a CNH.")

# Verifica se idade e maior ou igual
if idade >= MAIOR_IDADE:
    # Imprimi
    print("Maior de idade, pode tirar a CHN.")
# Verficia e idade e igual    
elif idade == IDADE_ESPECIAL:
    # Imprimi
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    # Imprimi
    print("Ainda não pode tirar a CNH.")