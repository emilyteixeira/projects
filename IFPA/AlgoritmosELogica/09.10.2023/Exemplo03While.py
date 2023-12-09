# While - Flag

sair = False

while sair == False:
  x = int(input('Digite um valor para elevar ao quadrado: '))
  q = x * x
  print('Valor ao quadrado: {}'.format(q))
  op = int(input('Digite 0 para Sair ou 1 para Continuar: '))
  if op == 0:
    sair = True
    print('Fim do Programa!')
