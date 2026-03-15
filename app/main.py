import gerenciador as ger
import modelo as m

def menu():
    opcao = input(print("\nOpções:\n"
        "1 - Inserir livros\n"
        "2 - Listar todos livros\n"
        "3 - Gerar relatório de livros\n"
        "4 - Sair\n"
        "Terminal: "))
    return opcao

def main():
    dao = ger.LivroDAO()
    while True:
        tarefa = menu()

        if tarefa == "1":
            print("\n-- Cadastrar Novo Livro --")
            titulo = input("Título: ")
            autor = input("Autor: ")
            preco = float(input("Preço: R$ "))
            estoque = int(input("Quantidade em Estoque: "))
            
            novo_livro = m.Livro(None, titulo, autor, preco, estoque, True)
            dao.inserir(novo_livro)
            print("\nLivro cadastrado com sucesso!")

        if tarefa == "2":
            dao.listar_todos()

        if tarefa == "3":
            dao.gerar_relatorio()

        if tarefa == "4":
            break

if __name__ == "__main__":
    main()
