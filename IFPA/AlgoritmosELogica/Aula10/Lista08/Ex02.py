# Escreva um algoritmo que realize o produto entre os 8 valores digitados pelo usuário.

produto = 1

for i in range(8):
    valor = float(input("Digite um valor: "))
    produto *= valor
print(f"O produto dos valores digitados é: {produto}")