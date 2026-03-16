from data_access_objects.clienteDAO import ClienteDAO
from data_access_objects.livroDAO import LivroDAO
from data_access_objects.pedidoDAO import PedidoDAO
from data_access_objects.pedidoItemDAO import PedidoItemDAO

import modelo as m


def main():
    while True:
        opcao = menu()

        if opcao == "1":
            dao = ClienteDAO()
            while True:
                tarefa = menuClientes()

                if tarefa == "1":
                    print("\n-- Cadastrar Novo Cliente --")
                    nome = ler_str("Nome: ")
                    email = ler_str_default("Email: ")
                    
                    novo_cliente = m.Cliente(id=None, nome=nome, email=email, ativo=True)
                    dao.inserir(novo_cliente)
                    print("\nCliente cadastrado com sucesso!")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do cliente que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        print("\nID inválido!\n")
                        continue
                    print("\n-- Digite os novos dados")

                    novo_nome = ler_str("Novo Nome: ")
                    novo_email = ler_str_default("Novo Email: ")
                    novo_ativo = input("Ativo? (s/N): ").lower() == 's'

                    #Cria o objeto Cliente com os novos dados
                    cliente_atualizado = m.Cliente(
                        id=id_alterar, 
                        nome=novo_nome,
                        email=novo_email,
                        ativo=novo_ativo
                    )
                    dao.alterar(cliente_atualizado)
                    print("Cliente atualizado com sucesso!")

                elif tarefa == "3":
                    dao.remover(input("Digite o ID do cliente que deseja remover: "))
                    print("\nCliente removido com sucesso!\n")

                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    print("Id   Nome       Email")
                    for i in range(len(resultado)):
                        print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}")

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do cliente que deseja buscar: "))
                    print(resultado)

                elif tarefa == "6":
                    nome = ler_str_default("Nome: ")
                    resultado = dao.buscar_nome(nome)
                    print("Id   Nome       Email")
                    for i in range(len(resultado)):
                        print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}")

                elif tarefa == "7":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de clientes: {resultado[0]}")

                elif tarefa == "0":
                    break

        elif opcao == "2":
            dao = LivroDAO()
            while True:
                tarefa = menuLivros()

                if tarefa == "1":
                    print("\n-- Cadastrar Novo Livro --")
                    titulo = ler_str("Título: ")
                    autor = ler_str("Autor: ")
                    preco = ler_float("Preço: R$ ")
                    estoque = ler_int_default("Quantidade em Estoque: ")
                    
                    novo_livro = m.Livro(id=None, titulo=titulo, autor=autor, preco=preco, estoque=estoque, ativo=True)
                    dao.inserir(novo_livro)
                    print("\nLivro cadastrado com sucesso!")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do livro que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        print("\nID inválido!\n")
                        continue
                    print("\n-- Digite os novos dados")

                    novo_titulo = ler_str("Novo Título: ")
                    novo_autor = ler_str("Novo Autor: ")
                    novo_preco = ler_float("Novo Preço: ")
                    novo_estoque = ler_int("Novo Estoque: ")
                    novo_ativo = input("Ativo? (s/N): ").lower() == 's'

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
                    
                elif tarefa == "3":
                    dao.remover(input("Digite o ID do livro que deseja remover: "))
                    print("\nLivro removido com sucesso!\n")
                    
                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    print("Id   Título      Autor       Preço   Estoque")
                    for i in range(len(resultado)):
                        print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}   {resultado[i][4]}")
                
                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do livro que deseja buscar: "))
                    print(resultado)
                
                elif tarefa == "6":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de livros: {resultado[0]}")
                    print(f"Valor total em estoque: R$ {resultado[1]}")
        
                elif tarefa == "0":
                    break

        elif opcao == "3":
            dao = PedidoDAO()
            while True:
                tarefa = menuPedidos()

                if tarefa == "1":
                    print("\n-- Fazer pedido --")
                    cliente_id = ler_float("ID do Cliente: ")
                    if dao.buscar_id(cliente_id) is None:
                        print("\nID inválido!\n")
                        continue
                    
                    novo_pedido = m.Pedido(id=None, cliente_id=cliente_id, data=None, estado="EM_ANDAMENTO", valor=0.0, pago=False)
                    dao.inserir(novo_pedido)
                    print("\nPedido aberto com sucesso!")

                elif tarefa == "2":
                    pass

                elif tarefa == "3":
                    resultado = dao.listar_todos()
                    print("Id   Cliente_Id   Data       Estado      Valor   Livro_Id")
                    for i in range(len(resultado)):
                        print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}       {resultado[i][4]}   {resultado[i][5]}")

                elif tarefa == "4":
                    resultado = dao.listar_cliente(input("ID do Cliente: "))
                    print("Id   Cliente_Id   Data       Estado      Valor   Livro_Id")
                    for i in range(len(resultado)):
                        print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}       {resultado[i][4]}   {resultado[i][5]}")

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do pedido que deseja buscar: "))
                    print(resultado)

                elif tarefa == "6":
                    dao.pagar(input("ID do pedido que deseja pagar: "))

                elif tarefa == "7":
                    pedido_id = input("ID do pedido: ")
                    estado_novo = input("Atualizar para qual estado?\n"
                    "1 - Em andamento\n"
                    "2 - Pronto\n"
                    "3 - Entregue\n"
                    "Terminal: ")
                    if estado_novo == "1":
                        estado_novo = "EM_ANDAMENTO"
                    elif estado_novo == "2":
                        estado_novo = "PRONTO"
                    elif estado_novo == "3":
                        estado_novo = "ENTREGUE"
                    
                    dao.atualizar_estado(pedido_id, estado_novo)

                elif tarefa == "8":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de pedidos: {resultado[0]}")
                    print(f"Valor total dos pedidos: R$ {resultado[1]}")

                elif tarefa == "0":
                    break

        elif opcao == "0":
            break


def menu():
    opcao = input("\nOpções:\n"
        "1 - Clientes\n"
        "2 - Livros\n"
        "3 - Pedidos\n"
        "0 - Sair\n"
        "Terminal: ")
    return opcao

def menuClientes():
    opcao = input("\nOpções:\n"
        "1 - Inserir cliente\n"
        "2 - Alterar cliente\n"
        "3 - Remover cliente\n"
        "4 - Listar todos clientes\n"
        "5 - Buscar por ID\n"
        "6 - Buscar por nome\n"
        "7 - Gerar relatório de clientes\n"
        "0 - Voltar\n"
        "Terminal: ")
    return opcao 


def menuLivros():
    opcao = input("\nOpções:\n"
        "1 - Inserir livro\n"
        "2 - Alterar livro\n"
        "3 - Remover livro\n"
        "4 - Listar todos livros\n"
        "5 - Buscar por ID\n"
        "6 - Gerar relatório de livros\n"
        "0 - Voltar\n"
        "Terminal: ")
    return opcao 


def menuPedidos():
    opcao = input("\nOpções:\n"
        "1 - Fazer pedido\n"
        "2 - Alterar pedido\n"
        "3 - Listar todos pedidos\n"
        "4 - Listar por cliente\n"
        "5 - Buscar por ID\n"
        "6 - Pagar pedido\n"
        "7 - Atualizar estado do pedido\n"
        "8 - Gerar relatório de pedidos\n"
        "0 - Voltar\n"
        "Terminal: ")
    return opcao 


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except:
            print("Erro: Valor inválido.")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("Erro: Valor inválido.")


def ler_int_default(mensagem):
    try:
        return int(input(mensagem))
    except:
        return 0


def ler_str(mensagem):
    while True:
        dado = input(mensagem)
        if dado == "":
            print("Erro: Valor inválido.")
            continue
        else:
            return dado
        

def ler_str_default(mensagem):
    dado = input(mensagem)
    if dado == "":
        dado = None
    return dado


if __name__ == "__main__":
    main()
