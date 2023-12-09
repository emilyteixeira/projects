# 3. Supermercado:
# Problema: Um caixa de supermercado precisa calcular o total a ser pago por um cliente. O
# cliente comprou N produtos, cada um com um preço diferente.
# Exercício: Escreva um algoritmo que receba o número de produtos e o preço de cada produto,
# calcule e exiba o total a ser pago.

# Minha Resolução

print('Supermercado Atacadão - Passe suas compras!')

numero_produtos = 0
contador = 0
total = 0
sair = False

while not sair:
    contador += 1
    numero_produtos = int(input('Digite o número de produtos a serem comprados: '))
    for i in range(numero_produtos):
        preco = float(input('Digite o preço do produto: '))
        total += preco
    print('Total a ser pago: R$', total)
    op = int(input('Digite 0 para Sair ou 1 para Continuar: '))
    if op == 0:
        sair = True
        print('Fim do Programa!')