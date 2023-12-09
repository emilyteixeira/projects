# 4. Agricultura:
# Problema: Um agricultor precisa calcular a quantidade de água necessária para irrigar sua
# plantação durante a estação seca. Ele sabe que cada planta precisa de 0,5 litros de água por
# dia.
# Exercício: Escreva um algoritmo que receba o número de plantas e o número de dias, calcule
# e exiba a quantidade total de água necessária.

# Minha Resolução
litros_por_planta = 0.5
total_plantas = int(input('Insira o número de plantas da sua plantação: '))
total_dias_seca = int(input('Insira o total de dias sem chover: '))

total_litros = (litros_por_planta * total_plantas) * total_dias_seca

print(f'A quantidade total de água necessária para {total_dias_seca} dias de seca é de {total_litros} litros!')
