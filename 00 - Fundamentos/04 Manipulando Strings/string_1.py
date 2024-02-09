# Instancia um variável string
nome = "NoMe"
# Imprimi em Maiúsculas
print(nome.upper())
# Imprimi em Minúsculo
print(nome.lower())
# Coloca a primeira Letra em Maiúsculas
print(nome.title())

# Instancia um variável string
texto = "  Olá mundo!    "
# Imprimindo texto com o (.) no final
print(texto + ".")
# Retira os espaço em brancos
print(texto.strip() + ".")
# Retira os espaço em brancos do lado direito
print(texto.rstrip() + ".")
# Retira os espaço em brancos do lado esquedo
print(texto.lstrip() + ".")

# Instancia um variável string
menu = "Python"
# Imprime ####Python####
print("####" + menu + "####")
# Imprime  (   Python   )
print(menu.center(14))
# Imprimi ####Python####
print(menu.center(14, "#"))
# Imprimi P-y-t-h-o-n
print("-".join(menu))