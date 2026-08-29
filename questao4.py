convidados = ["João", "Maria", "Pedro", "Ana", "Lucas"]

print("Lista atual de convidados:", convidados)

nome = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição em que ele será inserido: "))

convidados.insert(posicao, nome)

print("Lista atualizada:",convidados)

