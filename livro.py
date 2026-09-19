"""livro"""

class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def editar_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def mostrar_tudo(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Ano:", self.ano)


livro1 = livro("Casmurro", "Machado de Assis", 1899)

livro1.mostrar_tudo() 
livro1.editar_titulo("Dom Casmurro")
livro1.mostrar_tudo()