# Recebe o número de produtos
n_produtos = int(input("Digite o número de produtos: "))
# Inicializa o total
total = 0
# Calcula o total a ser pago
for i in range(n_produtos):
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    total += preco
# Exibe o resultado
print("Total a ser pago: R$", round(total, 2))