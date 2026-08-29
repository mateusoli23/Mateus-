nome = input("Digite o nome do aluno: ")

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Resultado")
print(f"Aluno: {nome}")
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
