# Escreva um algoritmo que eleva ao cubo todos os 10 valores digitados pelo usuário.

cubo = 0

for i in range(10):
    valor = float(input("Digite um valor: "))
    cubo = valor ** 3

    print(f"O cubo do valor digitado é: {cubo}")
