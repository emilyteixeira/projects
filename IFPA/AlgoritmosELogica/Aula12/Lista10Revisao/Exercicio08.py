# 8. Vendas:
# Problema: Uma loja oferece descontos progressivos conforme a quantidade de produtos
# comprados: 5% para 10 produtos, 10% para 20 produtos e 15% para 30 produtos ou mais.
# Exercício: Escreva um algoritmo que receba a quantidade de produtos e o preço unitário, e
# calcule o preço final com o desconto aplicado.

# Minha Resolução

quantidade_produtos = int(input('Quantidade de produtos: '))

for i in range(quantidade_produtos):
    preco_produto = float(input('Digite o preço do produto: '))
    if quantidade_produtos >= 10:
        desconto = 0.05
    elif quantidade_produtos >= 20:
        desconto = 0.1
    elif quantidade_produtos >= 30:
        desconto = 0.15
    else:
        desconto = 0
preco_final = (quantidade_produtos * preco_produto) * (desconto - 1)
print('O preço final já com o desconto aplicado é de R$', round(preco_final, 2))
