# 2. Construção:
# Problema: Um pedreiro precisa calcular a quantidade de tijolos necessários para construir
# uma parede. Cada tijolo tem as dimensões de 0.2m x 0.1m e a parede tem as dimensões de
# L metros de largura e A metros de altura.
# Exercício: Escreva um algoritmo que receba as dimensões da parede e calcule a quantidade
# de tijolos necessários.

# Minha Resolução

# Entradas
largura_tijolo = 0.2
altura_tijolo = 0.1
largura_parede = float(input('Insira um valor para a largura: '))
altura_parede = float(input('Insira um valor para a altura: '))

# Processamento
area_tijolo = (largura_tijolo * altura_tijolo)
area_parede = (largura_parede * altura_parede)
tijolos_necessarios = round(area_parede / area_tijolo)

# Saída
print(f'A quantidade de tijolos necessários para se construir essa parede é de {tijolos_necessarios}')
