n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero : "))

inicio = min(n1, n2)
fim = max(n1, n2)

for i in range(inicio +1, n2):
    print(i, end=" ")