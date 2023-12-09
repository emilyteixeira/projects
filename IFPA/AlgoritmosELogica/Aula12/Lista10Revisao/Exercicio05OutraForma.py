# Recebe a distância da viagem em km
distancia_km = float(input("Digite a distância da viagem em km: "))
# Custo do combustível por km (0.1 litros por km a R$5,00 por litro)
custo_por_km = 0.1 * 5.00
# Calcula o custo total
custo_total = distancia_km * custo_por_km
# Exibe o resultado
print("Custo total do combustível: R$", round(custo_total, 2))