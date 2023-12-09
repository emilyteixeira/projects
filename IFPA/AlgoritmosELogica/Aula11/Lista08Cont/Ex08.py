# Exercício 08
# Escreva um algoritmo que leia o nome e o número de filhos de 6 pessoas, imprimindo:
# Quantas pessoas têm filhos de 1 a 3 filhos.
# Quantas pessoas têm filhos de 4 a 7 filhos.
# Quantas pessoas têm filhos de 8 ou mais.
# Quantas pessoas não têm filhos.

# Minha Resposta:

# Contadores:
ate_3_filhos = 0
ate_7_filhos = 0
mais_de_7_filhos = 0
nenhum_filho = 0

# Laço:

for i in range(6):
    nome = input("Digite o nome: ")
    n_filhos = int(input("Digite o número de filhos: "))
    if (n_filhos >= 1) and (n_filhos <= 3):
        ate_3_filhos += 1

    elif n_filhos == 0:
        nenhum_filho += 1

    elif (n_filhos >= 4) and (n_filhos <= 7):
        ate_7_filhos += 1

    elif n_filhos >= 8:
        mais_de_7_filhos += 1

print(f'Quantidade de pessoas com até 3 filhos: {ate_3_filhos}')
print(f'Quantidade de pessoas com 3 a 7 filhos: {ate_7_filhos}')
print(f'Quantidade de pessoas com 8 filhos ou mais: {mais_de_7_filhos}')
print(f'Quantidade de pessoas com nenhum filho: {nenhum_filho}')
