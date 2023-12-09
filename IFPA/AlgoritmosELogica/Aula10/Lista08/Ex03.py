# Escreva um algoritmo que realize a média de 10 valores digitados pelo usuário

media = 0
soma = 0

for i in range(10):
    valor = float(input("Digite um valor: "))
    soma += valor
media = soma / 10
print(f"A média dos valores digitados é: {media}")
