# Recebe o número de plantas e dias
numero_plantas = int(input("Digite o número de plantas: "))
numero_dias = int(input("Digite o número de dias: "))
# Calcula a quantidade de água necessária
agua_necessaria = numero_plantas * numero_dias * 0.5 # 0.5 litros por planta por dia
# Exibe o resultado
print("Quantidade total de água necessária (em litros):", agua_necessaria)