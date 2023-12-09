# Recebe as dimensões da parede
largura_parede = float(input("Digite a largura da parede em metros: "))
altura_parede = float(input("Digite a altura da parede em metros: "))
# Dimensões do tijolo
largura_tijolo = 0.2 # em metros
altura_tijolo = 0.1 # em metros
# Calcula a quantidade de tijolos
tijolos_por_metro_quadrado = (1 / largura_tijolo) * (1 / altura_tijolo)
quantidade_tijolos = largura_parede * altura_parede * tijolos_por_metro_quadrado
# Exibe o resultado
print("Quantidade de tijolos necessários:", int(quantidade_tijolos))