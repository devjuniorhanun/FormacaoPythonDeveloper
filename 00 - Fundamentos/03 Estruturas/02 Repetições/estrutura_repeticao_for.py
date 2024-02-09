# Instancia texto com dados vindos pelo termina
texto = input("Informe um texto: ")
# Instancia uma constante
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    # Verifica se exite vogais nos dados vindos pelo termina 
    if letra.upper() in VOGAIS:
        print(letra, end="")
# Se o for não foi execuldado
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")