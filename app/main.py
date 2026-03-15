import gerenciador as ger
import modelo as m


def menu():
    print("\nOpções:\n"
        "1 - Inserir livros\n"
        "2 - Listar todos livros\n"
        "3 - Buscar por id\n"
        "4 - Gerar relatório de livros\n"
        "5 - Alterar livro\n"
        "6 - Remover livro\n"
        "7 - Sair\n"
        "Terminal: ")
    opcao = input()
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
            resultado = dao.buscar_id(input("Digite o ID do livro que deseja buscar: "))
            print(resultado)


        if tarefa == "4":
            dao.gerar_relatorio()

        if tarefa == "5":
            id_alterar = input("Digite o ID do livro que deseja alterar: ")
            if dao.buscar_id(id_alterar) is None:
                print("\nID inválido!\n")
                continue
            print("\n-- Digite os novos dados")

            novo_titulo = input("Novo Título: ")
            novo_autor = input("Novo Autor: ")
            novo_preco = input("Novo Preço: ")
            novo_estoque = input("Novo Estoque: ")
            novo_ativo = input("Ativo? (s/n): ").lower() == 's'

            #Cria o objeto Livro com os novos dados
    
            livro_atualizado = m.Livro(
                id=id_alterar, 
                titulo=novo_titulo, 
                autor=novo_autor, 
                preco=float(novo_preco), 
                estoque=int(novo_estoque),
                ativo=novo_ativo
            )

   
            dao.alterar(livro_atualizado)
            print("Livro atualizado com sucesso!")
        
        if tarefa == "6":
            dao.remover(input("Digite o ID do livro que deseja remover: "))
            print("\nLivro removido com sucesso!\n")
            

        if tarefa == "7":
            break

if __name__ == "__main__":
    main()
