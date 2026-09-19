"""criando a Classe pessoa"""

class pessoa:
    def __init__(self, n, i, p, a):#dentro dos parenteses ficam os parametros que sao os valores que o usuario vai me fornece 

        self.nome = n #self.nome e o atributo que vai armazena o parametro que o usuario fornecel
        self.idade = i
        self.peso = p 
        self.altura = a

    def apresentacao(self):
        print(f"o nome da pessoa consultada e {self.nome}; \nA idade dele(a) e {self.idade}")
    
    def fazer_aniversario(self):
        self.idade +=1 #esse metodo pega a idade do objeto e soma +1
        print(f"feliz aniversario, {self.nome}!!! sua nova idade agora e: {self.idade}.")


pessoa1 = pessoa("grace", 30, 55, 1.60)
pessoa2 = pessoa("alam", 25, 70, 1.80)

"""chamado os metodos"""
pessoa1.apresentacao()
pessoa2.fazer_aniversario()
pessoa1.apresentacao()