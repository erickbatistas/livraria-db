from app.data_access_objects.clienteDAO import ClienteDAO
from app.data_access_objects.livroDAO import LivroDAO
from app.data_access_objects.pedidoDAO import PedidoDAO
from app.data_access_objects.pedidoItemDAO import PedidoItemDAO
from app.data_access_objects.funcionarioDAO import FuncionarioDAO
from app.data_access_objects.fornecedorDAO import FornecedorDAO
from app.data_access_objects.relatorioDAO import RelatorioDAO
from tabulate import tabulate

from app import modelo as m
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
                    clientid = input("Digite o ID do cliente que deseja remover: ")
                    resultado = dao.buscar_id(clientid)

                    if resultado is None:
                        print("\nID inválido!\n")
                        continue
                    
                    else:
                        print("\nCliente removido:")
                        cabecalhos = ["ID", "Nome", "Email"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25]))
                        dao.remover(clientid)
                   

                    print("\n")

                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Nome", "Email"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25]))

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do cliente que deseja buscar: "))
                    if resultado is None:
                        print("\nCliente não encontrado.")
                    else:
                        cabecalhos = ["ID", "Nome", "Email"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25]))

                elif tarefa == "6":
                    nome = ler_str_default("Nome: ")
                    resultado = dao.buscar_nome(nome)
                    print(tabulate(resultado, ["ID", "Nome", "Email"], tablefmt="fancy_grid", maxcolwidths=[5, 20, 25] ))

                elif tarefa == "7":
                    resultado = dao.gerar_relatorio()
                    cabecalhos = ["ID", "Nome", "Email", "Total Pedidos", "Total Gasto", "Data Última Compra", "Ticket Médio"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8] ))

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
                    livroid = input("Digite o ID do livro que deseja remover: ")
                    resultado = dao.buscar_id(livroid)

                    if resultado is None:
                        print("\nID inválido!\n")
                        continue
                    else:
                        print("\nLivro removido:")
                        cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                        print(tabulate([resultado], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))
                        dao.remover(livroid)

                    print("\n")
                    
                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5] ))
                
                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do livro que deseja buscar: "))
                    if resultado is None:
                        print("\nLivro não encontrado.")
                    else:
                        cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                        print(tabulate([resultado], headers = cabecalhos,tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 10] ))
                
                elif tarefa == "6":
                    nome = ler_str("Buscar por nome: ")
                    resultado = dao.buscar_por_nome(nome)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "7":
                    categoria = ler_str("Buscar por categoria: ")
                    resultado = dao.buscar_por_categoria(categoria)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "8":
                    preco_min = ler_float("Preço mínimo: ")
                    preco_max = ler_float("Preço máximo: ")
                    resultado = dao.buscar_por_preco(preco_min, preco_max)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "9":
                    resultado = dao.buscar_fabricado_em_mari()
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "10":
                    resultado = dao.listar_pouco_estoque()
                    cabecalhos = ["ID", "Título", "Autor", "Estoque"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10]))

                elif tarefa == "11":
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
                    dao_cliente = ClienteDAO()
                    dao_funcionario = FuncionarioDAO()

                    print("\n-- Fazer pedido --")
                    cliente_id = ler_int("ID do Cliente: ")
                    if dao_cliente.buscar_id(cliente_id) is None:
                        print("\nID de cliente inválido!\n")
                        continue

                    funcionario_id = ler_int("ID do Vendedor (Funcionário): ")
                    if dao_funcionario.buscar_id(funcionario_id) is None:
                        print("\nID de funcionário inválido!\n")
                        continue
                    
                    # Lógica de Desconto
                    desconto = 0.0
                    print("\n-- Verificação de Desconto --")
                    torce_flamengo = input("O cliente torce para o Flamengo? (s/N): ").lower() == 's'
                    assiste_one_piece = input("O cliente assiste One Piece? (s/N): ").lower() == 's'
                    de_sousa = input("O cliente é de Sousa-PB? (s/N): ").lower() == 's'

                    if torce_flamengo or assiste_one_piece or de_sousa:
                        desconto = 0.1 # 10% de desconto
                        print(f"\nDesconto de {desconto*100}% aplicado!")

                    forma_pagamento = input("Forma de pagamento (cartao, boleto, pix, berries): ").strip().lower()

                    dao = PedidoDAO()
                    novo_pedido = m.Pedido(
                        id=None, 
                        cliente_id=cliente_id, 
                        funcionario_id=funcionario_id,
                        data=None, 
                        estado="EM_ANDAMENTO", 
                        valor=0.0, 
                        pago=False,
                        forma_pagamento=forma_pagamento,
                        desconto=desconto
                    )
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
                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5] ))

                elif tarefa == "4":
                    resultado = dao.listar_cliente(input("ID do Cliente: "))
                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"]
                    print(tabulate(resultado, headers = cabecalhos,tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 10] ))

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do pedido que deseja buscar: "))
                    if resultado is None:
                        print("\nPedido não encontrado.")
                    else:
                        cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5] ))

                elif tarefa == "6":
                    id_pagar = input("ID do pedido que deseja pagar: ")
                    pedido_para_pagar = dao.buscar_id(id_pagar)
                    if pedido_para_pagar is None:
                        print("\nPedido não encontrado.")
                    else:
                        cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"]
                        print(tabulate([pedido_para_pagar], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5]))
                        confirmar = input("Confirmar pagamento? (s/N): ").strip().lower() == 's'
                        if confirmar:
                            dao.pagar(id_pagar)
                            print("\nPedido pago com sucesso!")
                        else:
                            print("\nOperação cancelada pelo usuário.")

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

                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago"]
                    print(tabulate([pedido], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5]))
                    confirmar = input(f"Confirmar mudança para '{estado_novo}'? (s/N): ").strip().lower() == 's'
                    if confirmar:
                        dao.atualizar_estado(pedido_id, estado_novo)
                        print("\nEstado do pedido atualizado com sucesso!")
                    else:
                        print("\nOperação cancelada pelo usuário.")

                elif tarefa == "8":
                    resultado = dao.gerar_relatorio()
                    print(f"Total de pedidos: {resultado[0]}")
                    total_pedidos = resultado[1] if resultado[1] is not None else 0
                    print(f"Valor total dos pedidos: R$ {total_pedidos:.2f}")

                elif tarefa == "0":
                    break

                if tarefa != "0":
                    pausar()

        elif opcao == "4":
            dao = FuncionarioDAO()
            while True:
                tarefa = menuFuncionarios()

                if tarefa == "1":
                    print("\n-- Cadastrar Novo Funcionário --")
                    nome = ler_str("Nome: ")
                    cargo = ler_str("Cargo: ")
                    email = ler_str_default("Email: ")
                    
                    novo_funcionario = m.Funcionario(id=None, nome=nome, cargo=cargo, email=email, ativo=True)
                    dao.inserir(novo_funcionario)
                    print("\nFuncionário cadastrado com sucesso!")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do funcionário que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        print("\nID inválido!\n")
                        continue
                    print("\n-- Digite os novos dados")

                    novo_nome = ler_str("Novo Nome: ")
                    novo_cargo = ler_str("Novo Cargo: ")
                    novo_email = ler_str_default("Novo Email: ")
                    novo_ativo = input("Ativo? (s/N): ").lower() == 's'

                    funcionario_atualizado = m.Funcionario(
                        id=id_alterar, 
                        nome=novo_nome,
                        cargo=novo_cargo,
                        email=novo_email,
                        ativo=novo_ativo
                    )
                    dao.alterar(funcionario_atualizado)
                    print("Funcionário atualizado com sucesso!")

                elif tarefa == "3":
                    funcid = input("Digite o ID do funcionário que deseja remover: ")
                    resultado = dao.buscar_id(funcid)

                    if resultado is None:
                        print("\nID inválido!\n")
                        continue
                    
                    else:
                        print("\nFuncionário removido:")
                        cabecalhos = ["ID", "Nome", "Cargo", "Email"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 20, 25]))
                        dao.remover(funcid)
                   

                    print("\n")

                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Nome", "Cargo", "Email"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 20, 25]))

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do funcionário que deseja buscar: "))
                    if resultado is None:
                        print("\nFuncionário não encontrado.")
                    else:
                        cabecalhos = ["ID", "Nome", "Cargo", "Email"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 20, 25]))

                elif tarefa == "6":
                    print("\n-- Relatório de Vendas por Vendedor --")
                    mes = ler_int("Digite o mês (1-12): ")
                    ano = ler_int("Digite o ano: ")
                    dao_relatorio = RelatorioDAO()
                    resultado = dao_relatorio.gerar_relatorio_vendas_vendedor(mes, ano)
                    
                    if not resultado:
                        print(f"\nNenhuma venda encontrada para {mes}/{ano}.")
                    else:
                        cabecalhos = ["Vendedor", "Total de Vendas", "Valor Total Vendido"]
                        # Formata o valor total para duas casas decimais
                        resultado_formatado = [(nome, total, f"R$ {valor:.2f}" if valor else "R$ 0.00") for nome, total, valor in resultado]
                        print(tabulate(resultado_formatado, headers=cabecalhos, tablefmt="fancy_grid"))

                elif tarefa == "0":
                    break

                if tarefa != "0":
                    pausar()

        elif opcao == "5":
            dao = FornecedorDAO()
            while True:
                tarefa = menuFornecedores()

                if tarefa == "1":
                    print("\n-- Cadastrar Novo Fornecedor --")
                    nome = ler_str("Nome: ")
                    email = ler_str_default("Email: ")
                    telefone = ler_str_default("Telefone: ")
                    
                    novo_fornecedor = m.Fornecedor(id=None, nome=nome, email=email, telefone=telefone, ativo=True)
                    dao.inserir(novo_fornecedor)
                    print("\nFornecedor cadastrado com sucesso!")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do fornecedor que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        print("\nID inválido!\n")
                        continue
                    print("\n-- Digite os novos dados")

                    novo_nome = ler_str("Novo Nome: ")
                    novo_email = ler_str_default("Novo Email: ")
                    novo_telefone = ler_str_default("Novo Telefone: ")
                    novo_ativo = input("Ativo? (s/N): ").lower() == 's'

                    fornecedor_atualizado = m.Fornecedor(
                        id=id_alterar, 
                        nome=novo_nome,
                        email=novo_email,
                        telefone=novo_telefone,
                        ativo=novo_ativo
                    )
                    dao.alterar(fornecedor_atualizado)
                    print("Fornecedor atualizado com sucesso!")

                elif tarefa == "3":
                    fornecedorid = input("Digite o ID do fornecedor que deseja remover: ")
                    resultado = dao.buscar_id(fornecedorid)

                    if resultado is None:
                        print("\nID inválido!\n")
                        continue
                    
                    else:
                        print("\nFornecedor removido:")
                        cabecalhos = ["ID", "Nome", "Email", "Telefone"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 15]))
                        dao.remover(fornecedorid)
                   

                    print("\n")

                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Nome", "Email", "Telefone"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 15]))

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do fornecedor que deseja buscar: "))
                    if resultado is None:
                        print("\nFornecedor não encontrado.")
                    else:
                        cabecalhos = ["ID", "Nome", "Email", "Telefone"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 15]))

                elif tarefa == "0":
                    break

                if tarefa != "0":
                    pausar()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")
            pausar()


def carrinho(pedido_id):
    # valida pedido existe
    pedidoDao = PedidoDAO()
    pedido_valid = pedidoDao.buscar_id(pedido_id)
    if pedido_valid is None:
        print("\nPedido inválido ou não encontrado. Voltando ao menu.")
        pausar()
        return

    while True:
        dao = PedidoItemDAO()
        tarefa = menuPedidoItem()

        if tarefa == "1":
            print("\n-- Inserir livro no carrinho --")
            livro_id = ler_int("ID do livro: ")
            quantidade = ler_int("Quantidade de livros: ")
            try:
                novo_item = m.PedidoItem(id=None, pedido_id=pedido_id, livro_id=livro_id, quantidade=quantidade)
                sucesso = dao.inserir(novo_item)
                if sucesso:
                    print("\nLivro inserido no carrinho com sucesso!")
                else:
                    print("\nFalha ao inserir o livro no carrinho.")
            except Exception as e:
                print(f"\nErro ao inserir item no pedido: {e}")

  
        elif tarefa == "2":
           
            livro_id_str = input("Digite o ID do livro que deseja remover do carrinho: ")
            try:
                livro_id = int(livro_id_str)
            except:
                print("\nID inválido!\n")
                continue

            itens = dao.listar_pedido(pedido_id)
            item_encontrado = None
            for it in itens:
                # it[2] é o livro_id retornado por listar_pedido
                if it[2] == livro_id:
                    item_encontrado = it
                    break

            if item_encontrado is None:
                print("\nID do livro não encontrado no pedido!\n")
                continue

            try:
                # mostra o item que será removido
                print("\nRemovendo o seguinte item:")
                cabecalhos = ["ID", "Pedido ID", "Livro ID", "Título", "Autor", "Preço", "Quantidade"]
                print(tabulate([item_encontrado], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 10, 30, 20, 10, 10]))
                confirmar = input("Confirmar remoção? (s/N): ").strip().lower() == 's'
                if not confirmar:
                    print("\nOperação cancelada pelo usuário.\n")
                else:
                    dao.remover(pedido_id, livro_id)

                    # Verifica se foi removido
                    itens_apos = dao.listar_pedido(pedido_id)
                    still = any(it[2] == livro_id for it in itens_apos)
                    if not still:
                        print("\nLivro removido do carrinho com sucesso!\n")
                    else:
                        print("\nFalha ao remover o item do carrinho.\n")
            except Exception as e:
                print(f"\nErro ao remover item do pedido: {e}\n")

        elif tarefa == "3":
            resultado = dao.listar_pedido(pedido_id)
            cabecalhos = ["ID", "Pedido ID", "Livro ID", "Título", "Autor", "Preço", "Quantidade"]
            print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 10, 30, 20, 10, 10] ))
            pedidoDao = PedidoDAO()
            pedido = pedidoDao.buscar_id(pedido_id)
            if pedido is not None:
                print(f"\nValor total do pedido: R$ {pedido[4]:.2f}")
            else:
                print("\nNão foi possível obter o valor total do pedido.")
                
        elif tarefa == "4":
            dao = LivroDAO()
            resultado = dao.listar_todos()
            cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
            print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8] ))

        elif tarefa == "0":
            break
        if tarefa != "0":
            pausar()


def menu():
    limpar_tela()
    opcao = input("\nOpções:\n"
        "1 - Clientes\n"
        "2 - Livros\n"
        "3 - Pedidos\n"
        "4 - Funcionários\n"
        "5 - Fornecedores\n"
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
        "6 - Buscar por nome\n"
        "7 - Buscar por categoria\n"
        "8 - Buscar por faixa de preço\n"
        "9 - Buscar livros fabricados em Mari\n"
        "10 - Listar livros com pouco estoque\n"
        "11 - Gerar relatório de livros\n"
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
    opcao = input("\nOpções:\n"
        "1 - Inserir item\n"
        "2 - Remover item\n"
        "3 - Listar pedido\n"
        "4 - Listar livros\n"
        "0 - Voltar\n"
        "Terminal: ")
    return opcao


def menuFuncionarios():
    limpar_tela()
    opcao = input("\nOpções:\n"
        "1 - Inserir funcionário\n"
        "2 - Alterar funcionário\n"
        "3 - Remover funcionário\n"
        "4 - Listar todos funcionários\n"
        "5 - Buscar por ID\n"
        "6 - Relatório de vendas por vendedor\n"
        "0 - Voltar\n"
        "Terminal: ")
    return opcao

def menuFornecedores():
    limpar_tela()
    opcao = input("\nOpções:\n"
        "1 - Inserir fornecedor\n"
        "2 - Alterar fornecedor\n"
        "3 - Remover fornecedor\n"
        "4 - Listar todos fornecedores\n"
        "5 - Buscar por ID\n"
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





if __name__ == "__main__":
    main()
