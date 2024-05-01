aluno1 = (18632827, "John Lennon", 19, "Bacharelado em Ciência da Computação") # primeira tupla
aluno2 = 19817271, "Ringo Starr", 21, "Licenciatura em Matemática" # segunda tupla (sem parênteses)

print("Primeira tupla: ", aluno1, "Tipo: ", type(aluno1))
print("Segunda tupla: ", aluno2, "Tipo: ", type(aluno2))

print("Tamanho da primeira tupla: ", len(aluno1))

print("Valor de uma posição da primeira tupla: ", aluno1[1])

print("Uma fatia da segunda tupla: ", aluno2[1:3])

print("Todos os elementos da segunda tupla: ")
for elemento in aluno2:
    print(elemento)