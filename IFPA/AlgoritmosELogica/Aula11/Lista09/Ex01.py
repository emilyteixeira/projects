# Exercício 01

# Escreva um algoritmo que realize a soma entre os 6 valores digitados pelo usuário.

# Resposta:

soma = 0
for i in range(6):
    num = int(input('Digite um valor: '))
    soma += num

print(f'A soma dos números digitados é = {soma}')
