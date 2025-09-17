#Sistema de auto atendimento de cinema
ingressos = [15, 25, 32]
print("Boas vindas; Estamos felizes em te-lo por aqui;")
print("Temos atualmente ingressos disponiveis para 3 sessões dos filmes em cartaz, sendo respectivamente:")
print("filme 1:", ingressos[0], "filme 2:", ingressos[1], "filme 3:", ingressos[2])
idade = input("Insira idade por favor: ")
seguir_compra = ""

if int(idade) < 12:
    print ("Temos", ingressos[0], "ingressos disponiveis para o filme 1, de classificação livre;")
    seguir_compra = input("Prosseguir com a compra? ")
    if seguir_compra == "sim":
     ingressos[0] = ingressos[0] - 1
     print(ingressos)

elif int(idade) > 12 and int(idade) < 18:
    print ("Temos", ingressos[1], "ingressos disponiveis para o filme 2, de classificação para maiores de 12 anos;")
    seguir_compra = input("Prosseguir com a compra? ")
    if seguir_compra == "sim":
     ingressos[1] = ingressos[1] - 1
     print(ingressos)

elif int(idade) > 18:
    print ("Temos", ingressos[2], "ingressos disponiveis para o filme 3, de classificação para maiores de 18 anos;")
    seguir_compra = input("Prosseguir com a compra? ")
    if seguir_compra == "sim":
      ingressos[2] = ingressos[2] - 1
      print(ingressos)