# 5. Transporte:
# Problema: Uma empresa de transporte precisa calcular o custo total do combustível para uma
# viagem. O veículo consome 0,1 litros de combustível por km e o preço do litro do combustível
# é de R$5,00.
# Exercício: Escreva um algoritmo que receba a distância da viagem em km e calcule o custo
# total do combustível.

# Minha Resolução

combustivel_veiculo = 0.1
preco_combustivel = 5
distancia_total = float(input('Qual a distância total da viagem? (Em km) '))

custo_total = combustivel_veiculo * distancia_total * preco_combustivel
print(f'O custo total de combustível para esse veículo é de R$ {custo_total}!')
