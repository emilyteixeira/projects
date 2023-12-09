# Escreva um algoritmo que leia 10 números, determine quantos são positivos quantos
# são negativos e a soma dos valores positivos e o produto dos negativos. Informe os
# resultados.

# Contadores:
positivos = 0
negativos = 0

# Acumuladores:
somaPositivos = 0
produtoNegativos = 1

for i in range(10):
    valor = float(input("Digite um valor: "))
    if valor > 0:
        positivos += 1
        somaPositivos += valor
    elif valor < 0:
        negativos += 1
        produtoNegativos *= valor

print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(f'Soma dos Positivos: {somaPositivos}')
print(f'Produto dos Negativos: {produtoNegativos}')
