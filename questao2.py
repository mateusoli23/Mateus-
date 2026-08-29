lista = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

print("Números na ordem inversa:")

for i in reversed(lista):
    print(i)
