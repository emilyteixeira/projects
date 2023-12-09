# Escreva um algoritmo que leia o nome, o sexo e a idade de 8 pessoas. Mostrar quantas
# pessoas são do sexo masculino, quantas pessoas são do sexo feminino, quantas
# pessoas são menores de 18 anos e quantas são maiores ou iguais a 18 anos.

# Minha Resposta:

# Contadores:
homens = 0
mulheres = 0
menores = 0
maiores = 0

# Acumuladores:
qtdHomens = 0
qtdMulheres = 0
qtdMenores = 0
qtdMaiores = 0

for i in range(8):
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    idade = int(input("Digite a idade: "))

    if sexo.upper() == 'M':
        homens += 1

    elif sexo.upper() == 'F':
        mulheres += 1

    if idade >= 18:
        maiores += 1

    elif idade < 18:
        menores += 1

print(f'Quantidade de Homens: {qtdHomens}')
print(f'Quantidade de Mulheres: {qtdMulheres}')
print(f'Quantidade de Pessoas Menores de 18 anos: {qtdMenores}')
print(f'Quantidade de Pessoas Maiores ou Iguais a 18 anos: {qtdMaiores}')

# Correção: Acertei
