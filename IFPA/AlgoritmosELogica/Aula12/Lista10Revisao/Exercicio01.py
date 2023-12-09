# 1. Nutrição:
# Problema: Um nutricionista precisa calcular o Índice de Massa Corporal (IMC) de um
# paciente. O IMC é calculado dividindo o peso do paciente (em kg) pela altura ao quadrado
# (em metros).
# Exercício: Escreva um algoritmo que receba o peso e a altura de um paciente, calcule e exiba
# o IMC.

# Minha Resolução
print('Calculadora de IMC')

# Entradas
peso = float(input('Insira o peso: '))
altura = float(input('Agora, insira a altura: '))

# Processamento
# imc = peso / (altura ** 2)
imc = peso / (altura * altura)

# Saída
print(f'Seu IMC é de {imc}!')

# Sugestão:
# Adicionar uma tomada de decisão para imprimir o nível do IMC calculado

# Dúvida:
# Como deixar apenas 2 casas decimais?
