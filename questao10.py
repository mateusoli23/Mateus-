numero = int(input("Montar tabuada de: "))
inicio = int(input("começa em:"))
fim = int(input("termina em: "))

print(f"vou monar a taboada {numero} começa em {inicio} termina em {fim}:")

for i in range(inicio , fim +1):
    resul = numero * i
    print(f"{numero} x {i} = {resul}:")