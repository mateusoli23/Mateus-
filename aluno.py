class Aluno:
    def __init__(self, nome, matricula, nota1, nota2, nota3, nota4, nota5):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5) / 5
        return media

    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "Aluno aprovado!"
        else:
            return "Aluno reprovado!"


aluno1 = Aluno("João", 12345, 8, 7, 9, 6, 10)
print("Nome:", aluno1.nome)
print("Média:", aluno1.calcular_media())
print(aluno1.verificar_aprovacao())