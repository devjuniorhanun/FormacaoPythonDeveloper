# Cria um arry com os Meses
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# Instancia a variável com dos dados vindos do terminal
m = int(input())
# Percorre o array
if m in months.keys():
    # Imprimi o mês correspondente
    print(months[m])