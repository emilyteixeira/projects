# 6. Energia:
# Problema: Um gerente de facilities quer calcular o custo mensal de energia elétrica de um
# edifício. O custo por kilowatt-hora (kWh) é R$0,50.
# Exercício: Escreva um algoritmo que receba o número de kWh consumidos e calcule o custo
# total.

# Minha Resolução

quilowatt_hora = 0.5
kw_mensal = float(input('Qual a quantidade de kWh consumidos no mês? '))

# Dúvida: qual o cálculo?
custo_total = quilowatt_hora * kw_mensal
print(f'O custo total de energia elétrica para esse edifício é de R$ {custo_total}!')
