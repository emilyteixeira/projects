# Exercício 07

# Escreva um algoritmo para imprimir a tabuada de um número.

# Minha Resposta:
numero = int(input('Digite um número: '))
tabuada = 1

for i in range(0, 9):
    tabuada = i * numero
    print(f'{i} x {numero} = {tabuada}')

# Resposta do Professor:

# num = int(input('Digite um número para a Tabuada: '))
# for i in range(1, 11):
#    print(f'{num} x {i} = {num * i}')
