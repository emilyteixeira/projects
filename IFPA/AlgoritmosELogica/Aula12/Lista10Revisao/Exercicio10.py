# 10. Meteorologia:
# Problema: Um meteorologista quer calcular a média de temperaturas de uma semana.
# Exercício: Escreva um algoritmo que receba as temperaturas de cada dia da semana e
# calcule a média.

# Minha Resolução:

# Inicializa a soma
soma = 0

# Recebe as temperaturas e armazena a soma delas na variável soma
for i in range(1, 8):
    temperatura_maxima_diaria = float(input(f'Qual a temperatura máxima registrada no dia {i}? '))
    soma += temperatura_maxima_diaria

# Calcula a média dessas temperaturas
media = soma / 7
print('Média das temperaturas apresentadas =', round(media, 2), '°C.')
