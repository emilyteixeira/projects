# 7. Educação:
# Problema: Um professor precisa calcular a média final de um aluno que fez 4 provas durante
# o semestre.
# Exercício: Escreva um algoritmo que receba as notas das 4 provas e calcule a média final do
# aluno.

# Minha Resolução

prova1 = float(input('Digite a nota da Prova 1: '))
prova2 = float(input('Digite a nota da Prova 2: '))
prova3 = float(input('Digite a nota da Prova 3: '))
prova4 = float(input('Digite a nota da Prova 4: '))

media = (prova1 + prova2 + prova3 + prova4) / 4

print('Média final do(a) aluno(a) =', media)