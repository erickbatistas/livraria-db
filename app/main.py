from data_access_objects.clienteDAO import ClienteDAO
from data_access_objects.livroDAO import LivroDAO
from data_access_objects.pedidoDAO import PedidoDAO
from data_access_objects.pedidoItemDAO import PedidoItemDAO

import modelo as m
import os


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

                    # Cria o objeto Cliente com os novos dados
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
                    exibir_tabela(
                        ["ID", "Nome", "Email"],
                        resultado,
                    )

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do cliente que deseja buscar: "))
                    if resultado is None:
                        print("\nCliente não encontrado.")
                    else:
                        exibir_tabela(["ID", "Nome", "Email"], [resultado])

                elif tarefa == "6":
                    nome = ler_str_default("Nome: ")
                    resultado = dao.buscar_nome(nome)
                    exibir_tabela(["ID", "Nome", "Email"], resultado)

                elif tarefa == "7":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de clientes: {resultado[0]}")

                elif tarefa == "0":
                    break

                if tarefa != "0":
                    pausar()

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

                    # Cria o objeto Livro com os novos dados
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
                    exibir_tabela(
                        ["ID", "Título", "Autor", "Preço", "Estoque"],
                        resultado,
                    )
                
                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do livro que deseja buscar: "))
                    if resultado is None:
                        print("\nLivro não encontrado.")
                    else:
                        exibir_tabela(["ID", "Título", "Autor", "Preço", "Estoque"], [resultado])
                
                elif tarefa == "6":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de livros: {resultado[0]}")
                    total_estoque = resultado[1] if resultado[1] is not None else 0
                    print(f"Valor total em estoque: R$ {total_estoque:.2f}")
        
                elif tarefa == "0":
                    break

                if tarefa != "0":
                    pausar()

        elif opcao == "3":
            dao = PedidoDAO()
            while True:
                tarefa = menuPedidos()

                if tarefa == "1":
                    dao = ClienteDAO() # Hack
                    print("\n-- Fazer pedido --")
                    cliente_id = ler_int("ID do Cliente: ")
                    if dao.buscar_id(cliente_id) is None:
                        print("\nID inválido!\n")
                        continue
                    
                    dao = PedidoDAO() # Hack
                    novo_pedido = m.Pedido(id=None, cliente_id=cliente_id, data=None, estado="EM_ANDAMENTO", valor=0.0, pago=False)
                    dao.inserir(novo_pedido)
                    print("\nPedido aberto com sucesso!")
                    pedido_id = dao.id_ultimo_pedido()
                    
                    carrinho(pedido_id)

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do pedido que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        print("\nID inválido!\n")
                        continue

                    carrinho(id_alterar)

                elif tarefa == "3":
                    resultado = dao.listar_todos()
                    exibir_tabela(["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"],resultado,)

                elif tarefa == "4":
                    resultado = dao.listar_cliente(input("ID do Cliente: "))
                    exibir_tabela(["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"],resultado,)

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do pedido que deseja buscar: "))
                    if resultado is None:
                        print("\nPedido não encontrado.")
                    else:
                        exibir_tabela(["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"], [resultado])

                elif tarefa == "6":
                    dao.pagar(input("ID do pedido que deseja pagar: "))
                    print("\nPedido pago com sucesso!")

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
                    pedido = dao.buscar_id(pedido_id)
                    if pedido is None:
                        print("\nID do pedido inválido!\n")
                        continue

                    # Só permite mudar para PRONTO/ENTREGUE se o pedido já estiver pago
                    if estado_novo in ("PRONTO", "ENTREGUE") and not pedido[5]:
                        print("\nOperação não permitida: o pedido precisa ser pago antes de enviar/entregar.\n")
                        continue

                    dao.atualizar_estado(pedido_id, estado_novo)
                    print("\nEstado do pedido atualizado com sucesso!")

                elif tarefa == "8":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de pedidos: {resultado[0]}")
                    total_pedidos = resultado[1] if resultado[1] is not None else 0
                    print(f"Valor total dos pedidos: R$ {total_pedidos:.2f}")

                elif tarefa == "0":
                    break

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")
            pausar()


def carrinho(pedido_id):
    while True:
        dao = PedidoItemDAO()
        tarefa = menuPedidoItem()

        if tarefa == "1":
            print("\n-- Inserir livro no carrinho --")
            livro_id = ler_int("ID do livro: ")
            quantidade = ler_int("Quantidade de livros: ")
            
            novo_item = m.PedidoItem(id=None, pedido_id=pedido_id, livro_id=livro_id, quantidade=quantidade)
            sucesso = dao.inserir(novo_item)
            if sucesso:
                print("\nLivro inserindo no carrinho com sucesso!")

        elif tarefa == "2":
           
            livro_id_str = input("Digite o ID do livro que deseja remover do carrinho: ")
            try:
                livro_id = int(livro_id_str)
            except:
                print("\nID inválido!\n")
                continue

            itens = dao.listar_pedido(pedido_id)
            existe = False
            for item in itens:
                # item[2] é o livro_id retornado por listar_pedido
                if item[2] == livro_id:
                    existe = True
                    break

            if not existe:
                print("\nID do livro não encontrado no pedido!\n")
                continue

            dao.remover(pedido_id, livro_id)
            print("\nLivro removido do carrinho com sucesso!\n")

        elif tarefa == "3":
            resultado = dao.listar_pedido(pedido_id)
            exibir_tabela(["ID", "Pedido ID", "Livro ID", "Título", "Autor", "Preço", "Quantidade"],resultado,)
            pedidoDao = PedidoDAO()
            pedido = pedidoDao.buscar_id(pedido_id)
            if pedido is not None:
                print(f"\nValor total do pedido: R$ {pedido[4]:.2f}")
            else:
                print("\nNão foi possível obter o valor total do pedido.")

        elif tarefa == "4":
            dao = LivroDAO()
            resultado = dao.listar_todos()
            exibir_tabela(["ID", "Título", "Autor", "Preço", "Estoque"],resultado,)

        elif tarefa == "0":
            break


def menu():
    limpar_tela()
    opcao = input("\nOpções:\n"
        "1 - Clientes\n"
        "2 - Livros\n"
        "3 - Pedidos\n"
        "0 - Sair\n"
        "Terminal: ")
    return opcao

def menuClientes():
    limpar_tela()
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
    limpar_tela()
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
    limpar_tela()
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


def menuPedidoItem():
    limpar_tela()
    opcao = input("\nOpções:\n"
        "1 - Inserir item\n"
        "2 - Remover item\n"
        "3 - Listar pedido\n"
        "4 - Listar livros\n"
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


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")


def formatar_celula(valor):
    if valor is None:
        return "-"
    if isinstance(valor, bool):
        return "Sim" if valor else "Não"
    if isinstance(valor, float):
        return f"{valor:.2f}"
    return str(valor)


def exibir_tabela(cabecalhos, linhas):
    if not linhas:
        print("\nNenhum registro encontrado.")
        return

    linhas_formatadas = [[formatar_celula(celula) for celula in linha] for linha in linhas]

    larguras = []
    for indice, cabecalho in enumerate(cabecalhos):
        maior_linha = max(len(linha[indice]) for linha in linhas_formatadas)
        larguras.append(max(len(cabecalho), maior_linha))

    separador = "+-" + "-+-".join("-" * largura for largura in larguras) + "-+"

    print()
    print(separador)
    print("| " + " | ".join(cabecalho.ljust(larguras[i]) for i, cabecalho in enumerate(cabecalhos)) + " |")
    print(separador)
    for linha in linhas_formatadas:
        print("| " + " | ".join(linha[i].ljust(larguras[i]) for i in range(len(cabecalhos))) + " |")
    print(separador)


if __name__ == "__main__":
    main()
