class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        # Questão 1
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        # Questão 2
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Disponível: {self.disponivel}"

    def emprestar(self):
        # Questão 3
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    @staticmethod
    def verificar_disponibilidade(ano):
        # Questão 4
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]


# Questões 5, 6, 7 e 8


if __name__ == "__main__":
    livro1 = Livro("A Culpa é das Estrelas", "John Green", 2012)
    livro2 = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954)


    print(livro1)
    print(livro2)


    livro1.emprestar()
    print(f"Após empréstimo, disponível: {livro1.disponivel}")


    ano_verificar = 1954
    livros_disponiveis = Livro.verificar_disponibilidade(ano_verificar)
    print(f"Livros disponíveis em {ano_verificar}:")
    for livro in livros_disponiveis:
        print(livro)
