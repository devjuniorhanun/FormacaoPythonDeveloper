# Instancia a variável com dos dados vindos do terminal
n = int(input())

# Cria um laço de Repetição com o número passado
for _ in range(n):
    # Instancia duas variável com dos dados vindos do terminal
    a, b = input().strip().split(' ')

    # Verifica se b e maior que a
    if(len(b) > len(a)):
        # Imprimi
        print('nao encaixa')
    # Se b e maior que a    
    else:
        a = a[(len(a) - len(b)):]
        # Imprimi
        print('encaixa' if a == b else 'nao encaixa')