try:
    from app.data_access_objects.clienteDAO import ClienteDAO
    from app.data_access_objects.livroDAO import LivroDAO
    from app.data_access_objects.pedidoDAO import PedidoDAO
    from app.data_access_objects.pedidoItemDAO import PedidoItemDAO
    from app.data_access_objects.funcionarioDAO import FuncionarioDAO
    from app.data_access_objects.fornecedorDAO import FornecedorDAO
    from app.data_access_objects.relatorioDAO import RelatorioDAO
except ImportError:
    from data_access_objects.clienteDAO import ClienteDAO
    from data_access_objects.livroDAO import LivroDAO
    from data_access_objects.pedidoDAO import PedidoDAO
    from data_access_objects.pedidoItemDAO import PedidoItemDAO
    from data_access_objects.funcionarioDAO import FuncionarioDAO
    from data_access_objects.fornecedorDAO import FornecedorDAO
    from data_access_objects.relatorioDAO import RelatorioDAO
from tabulate import tabulate

try:
    from app import modelo as m
except ImportError:
    import modelo as m
import os


def main():
    while True:
        opcao = menu()

        if opcao == "1":
            limpar_tela()
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
                        limpar_tela()
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
                        limpar_tela()
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
                    limpar_tela()
                    break

                if tarefa != "0":
                    pausar()
                    limpar_tela()

        elif opcao == "2":
            limpar_tela()
            dao = LivroDAO()
            while True:
                tarefa = menuLivros()

                if tarefa == "1":
                    print("\n-- Cadastrar Novo Livro --")
                    titulo = ler_str("Título: ")
                    autor = ler_str("Autor: ")
                    preco = ler_float("Preço: R$ ")
                    estoque = ler_int_default("Quantidade em Estoque: ")
                    categoria = ler_str_default("Categoria: ")
                    fabricado_em_mari = input("Fabricado em Mari? (s/N): ").strip().lower() == 's'
                    
                    novo_livro = m.Livro(
                        id=None,
                        titulo=titulo,
                        autor=autor,
                        preco=preco,
                        estoque=estoque,
                        ativo=True,
                        categoria=categoria,
                        fabricado_em_mari=fabricado_em_mari,
                    )
                    dao.inserir(novo_livro)
                    print("\nLivro cadastrado com sucesso!")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do livro que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        limpar_tela()
                        print("\nID inválido!\n")
                        continue
                    print("\n-- Digite os novos dados")

                    novo_titulo = ler_str("Novo Título: ")
                    novo_autor = ler_str("Novo Autor: ")
                    novo_preco = ler_float("Novo Preço: ")
                    novo_estoque = ler_int("Novo Estoque: ")
                    nova_categoria = ler_str_default("Nova Categoria: ")
                    novo_fabricado_em_mari = input("Fabricado em Mari? (s/N): ").strip().lower() == 's'
                    novo_ativo = input("Ativo? (s/N): ").lower() == 's'

                    # Cria o objeto Livro com os novos dados
                    livro_atualizado = m.Livro(
                        id=id_alterar, 
                        titulo=novo_titulo, 
                        autor=novo_autor, 
                        preco=float(novo_preco), 
                        estoque=int(novo_estoque),
                        ativo=novo_ativo,
                        categoria=nova_categoria,
                        fabricado_em_mari=novo_fabricado_em_mari,
                    )
                    dao.alterar(livro_atualizado)
                    print("Livro atualizado com sucesso!")
                    
                elif tarefa == "3":
                    livroid = input("Digite o ID do livro que deseja remover: ")
                    resultado = dao.buscar_id(livroid)

                    if resultado is None:
                        limpar_tela()
                        print("\nID inválido!\n")
                        continue
                    else:
                        print("\nLivro removido:")
                        cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                        print(tabulate([resultado], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))
                        dao.remover(livroid)

                    print("\n")
                    
                elif tarefa == "4":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5] ))
                
                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do livro que deseja buscar: "))
                    if resultado is None:
                        print("\nLivro não encontrado.")
                    else:
                        cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                        print(tabulate([resultado], headers = cabecalhos,tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 10] ))
                
                elif tarefa == "6":
                    nome = ler_str("Buscar por nome: ")
                    resultado = dao.buscar_por_nome(nome)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "7":
                    categoria = ler_str("Buscar por categoria: ")
                    resultado = dao.buscar_por_categoria(categoria)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "8":
                    preco_min = ler_float("Preço mínimo: ")
                    preco_max = ler_float("Preço máximo: ")
                    resultado = dao.buscar_por_preco(preco_min, preco_max)
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
                    print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

                elif tarefa == "9":
                    resultado = dao.buscar_fabricado_em_mari()
                    cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque", "Categoria", "Fabricado em Mari"]
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
                    limpar_tela()
                    break

                if tarefa != "0":
                    pausar()
                    limpar_tela()

        elif opcao == "3":
            limpar_tela()
            dao = PedidoDAO()
            while True:
                tarefa = menuPedidos()

                if tarefa == "1":
                    dao_cliente = ClienteDAO()
                    dao_funcionario = FuncionarioDAO()
                    dao_item = PedidoItemDAO()

                    print("\n-- Fazer pedido --")
                    cliente_id = ler_int("ID do Cliente: ")
                    if dao_cliente.buscar_id(cliente_id) is None:
                        limpar_tela()
                        print("\nID de cliente inválido!\n")
                        continue

                    funcionario_id = ler_int("ID do Vendedor (Funcionário): ")
                    if dao_funcionario.buscar_id(funcionario_id) is None:
                        limpar_tela()
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

                    forma_pagamento = ler_forma_pagamento()

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
                    if not dao_item.listar_pedido(pedido_id):
                        dao.remover(pedido_id)
                        print("\nPedido cancelado: toda compra precisa ter pelo menos 1 item.")

                elif tarefa == "2":
                    id_alterar = input("Digite o ID do pedido que deseja alterar: ")
                    if dao.buscar_id(id_alterar) is None:
                        limpar_tela()
                        print("\nID inválido!\n")
                        continue

                    carrinho(id_alterar)

                elif tarefa == "3":
                    resultado = dao.listar_todos()
                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                    print(tabulate(resultado, headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5, 10, 12] ))

                elif tarefa == "4":
                    resultado = dao.listar_cliente(input("ID do Cliente: "))
                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                    print(tabulate(resultado, headers = cabecalhos,tablefmt="fancy_grid", maxcolwidths=[5, 20, 25, 10, 10, 5, 10, 12] ))

                elif tarefa == "5":
                    resultado = dao.buscar_id(input("Digite o ID do pedido que deseja buscar: "))
                    if resultado is None:
                        print("\nPedido não encontrado.")
                    else:
                        cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                        print(tabulate([resultado], headers = cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5, 10, 12] ))

                elif tarefa == "6":
                    id_pagar = input("ID do pedido que deseja pagar: ")
                    pedido_para_pagar = dao.buscar_id(id_pagar)
                    if pedido_para_pagar is None:
                        print("\nPedido não encontrado.")
                    else:
                        cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                        print(tabulate([pedido_para_pagar], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5, 10, 12]))
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
                        limpar_tela()
                        print("\nID do pedido inválido!\n")
                        continue

                    # Só permite mudar para PRONTO/ENTREGUE se o pedido já estiver pago
                    if estado_novo in ("PRONTO", "ENTREGUE") and not pedido[5]:
                        limpar_tela()
                        print("\nOperação não permitida: o pedido precisa ser pago antes de enviar/entregar.\n")
                        continue

                    cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                    print(tabulate([pedido], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5, 10, 12]))
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
                    limpar_tela()
                    break

                if tarefa != "0":
                    pausar()
                    limpar_tela()

        elif opcao == "4":
            limpar_tela()
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
                        limpar_tela()
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
                        limpar_tela()
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

                elif tarefa == "7":
                    print("\n-- Produtos com Pouco Estoque (< 5) --")
                    dao_livro = LivroDAO()
                    resultado = dao_livro.listar_pouco_estoque()
                    if not resultado:
                        print("Nenhum produto com estoque baixo no momento.")
                    else:
                        cabecalhos = ["ID", "Título", "Autor", "Estoque"]
                        print(tabulate(resultado, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10]))

                elif tarefa == "0":
                    limpar_tela()
                    break

                if tarefa != "0":
                    pausar()
                    limpar_tela()

        elif opcao == "5":
            limpar_tela()
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
                        limpar_tela()
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
                        limpar_tela()
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
                    limpar_tela()
                    break

                if tarefa != "0":
                    pausar()
                    limpar_tela()
        
        elif opcao == "6":
            limpar_tela()
            iniciar_area_cliente()

        elif opcao == "0":
            print("Saindo...")
            break

def menu():
    limpar_tela()
    print("====================================")
    print("      LIVRARIA DB - MENU")
    print("====================================")
    print("1 - Clientes")
    print("2 - Livros")
    print("3 - Pedidos")
    print("4 - Funcionários")
    print("5 - Fornecedores")
    print("6 - Área do Cliente")
    print("0 - Sair")
    return input("Terminal: ")

def menuAreaCliente():
    limpar_tela()
    print("\n-- ÁREA DO CLIENTE --")
    print("1 - Ver meus dados cadastrais")
    print("2 - Alterar meus dados cadastrais")
    print("3 - Ver meus pedidos")
    print("0 - Voltar ao menu principal")
    return input("Terminal: ")

def iniciar_area_cliente():
    cliente_dao = ClienteDAO()
    pedido_dao = PedidoDAO()

    cliente_id = ler_int("\nPara começar, digite o seu ID de cliente: ")
    cliente = cliente_dao.buscar_id(cliente_id)

    if cliente is None:
        print("\nID de cliente não encontrado.")
        pausar()
        return

    print(f"\nBem-vindo(a), {cliente[1]}!")
    pausar()

    while True:
        tarefa = menuAreaCliente()

        if tarefa == "1":
            print("\n-- Meus Dados Cadastrais --")
            # Re-busca os dados para garantir que estão atualizados
            cliente = cliente_dao.buscar_id(cliente_id) 
            cabecalhos = ["ID", "Nome", "Email"]
            print(tabulate([cliente], headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 20, 25]))

        elif tarefa == "2":
            print("\n-- Alterar Meus Dados --")
            print("Deixe em branco para não alterar.")
            
            novo_nome = ler_str_default(f"Nome ({cliente[1]}): ")
            novo_email = ler_str_default(f"Email ({cliente[2]}): ")

            # Se o campo foi deixado em branco, mantém o valor antigo
            if not novo_nome:
                novo_nome = cliente[1]
            if not novo_email:
                novo_email = cliente[2]

            cliente_atualizado = m.Cliente(
                id=cliente_id,
                nome=novo_nome,
                email=novo_email,
                ativo=True # Mantém o cliente ativo
            )
            cliente_dao.alterar(cliente_atualizado)
            
            # Atualiza a variável local 'cliente' para refletir a mudança
            cliente = cliente_dao.buscar_id(cliente_id) 
            print("\nDados atualizados com sucesso!")

        elif tarefa == "3":
            print("\n-- Meus Pedidos --")
            pedidos = pedido_dao.listar_cliente(cliente_id)
            if not pedidos:
                print("Você ainda não tem nenhum pedido.")
            else:
                cabecalhos = ["ID", "Cliente ID", "Data", "Estado", "Valor", "Pago", "Forma", "Confirmação"]
                print(tabulate(pedidos, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 10, 12, 12, 10, 5, 10, 12]))

        elif tarefa == "0":
            limpar_tela()
            break
        
        if tarefa != "0":
            pausar()
            limpar_tela()

def menuRelatorios():
    print("\n-- RELATÓRIOS --")
    print("1 - Relatório de Clientes")
    print("2 - Relatório de Livros")
    print("3 - Relatório de Vendas por Vendedor")
    print("4 - Relatório Geral de Pedidos")
    print("0 - Voltar")
    return input("Terminal: ")

def menuClientes():
    print("\n-- CLIENTES --")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Remover")
    print("4 - Listar todos clientes")
    print("5 - Buscar por ID")
    print("6 - Buscar por nome")
    print("7 - Relatório de Clientes")
    print("0 - Voltar")
    return input("Terminal: ")

def menuLivros():
    print("\n-- LIVROS --")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Remover")
    print("4 - Listar todos livros")
    print("5 - Buscar por ID")
    print("6 - Buscar por nome")
    print("7 - Buscar por categoria")
    print("8 - Buscar por faixa de preço")
    print("9 - Buscar livros fabricados em Mari")
    print("10 - Listar livros com pouco estoque")
    print("11 - Gerar relatório de livros")
    print("0 - Voltar")
    return input("Terminal: ")

def menuPedidos():
    print("\n-- PEDIDOS --")
    print("1 - Fazer pedido")
    print("2 - Alterar pedido")
    print("3 - Listar todos pedidos")
    print("4 - Listar por cliente")
    print("5 - Buscar por ID")
    print("6 - Pagar pedido")
    print("7 - Atualizar estado do pedido")
    print("8 - Gerar relatório de pedidos")
    print("0 - Voltar")
    return input("Terminal: ")

def menuFuncionarios():
    print("\n-- FUNCIONÁRIOS --")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Remover")
    print("4 - Listar todos")
    print("5 - Buscar por ID")
    print("6 - Relatório de Vendas")
    print("7 - Produtos com pouco estoque")
    print("0 - Voltar")
    return input("Terminal: ")

def menuFornecedores():
    print("\n-- FORNECEDORES --")
    print("1 - Cadastrar")
    print("2 - Alterar")
    print("3 - Remover")
    print("4 - Listar todos")
    print("5 - Buscar por ID")
    print("0 - Voltar")
    return input("Terminal: ")

def menuPedidoItem():
    print("\n1 - Inserir item")
    print("2 - Remover item")
    print("3 - Listar itens do pedido")
    print("4 - Listar livros disponíveis")
    print("0 - Voltar")
    return input("Terminal: ")

def carrinho(pedido_id):
    dao_item = PedidoItemDAO()
    dao_livro = LivroDAO()

    print("\n-- Carrinho de Compras --")
    while True:
        opcao = menuPedidoItem()

        if opcao == "1":
            print("\n-- Inserir item --")
            livro_id = input("ID do Livro: ")
            if dao_livro.buscar_id(livro_id) is None:
                limpar_tela()
                print("\nLivro não encontrado.")
                continue

            quantidade = ler_int("Quantidade: ")
            if quantidade <= 0:
                limpar_tela()
                print("Quantidade inválida.")
                continue

            item = m.PedidoItem(pedido_id=pedido_id, livro_id=livro_id, quantidade=quantidade)
            inserido = dao_item.inserir(item)
            if inserido:
                print("\nItem inserido com sucesso!")

        elif opcao == "2":
            print("\n-- Remover item --")
            livro_id = ler_int("ID do Livro: ")
            if dao_livro.buscar_id(livro_id) is None:
                limpar_tela()
                print("\nLivro não encontrado.")
                continue

            itens_atuais = dao_item.listar_pedido(pedido_id)
            itens_do_livro = [item for item in itens_atuais if item[2] == livro_id]
            if len(itens_atuais) == 1 and itens_do_livro:
                limpar_tela()
                print("\nOperação não permitida: o pedido deve ter pelo menos 1 item.")
                continue

            removido = dao_item.remover(pedido_id, livro_id)
            if removido:
                print("\nItem removido com sucesso!")
            else:
                print("\nItem não encontrado neste pedido.")

        elif opcao == "3":
            print("\n-- Itens do pedido --")
            itens = dao_item.listar_pedido(pedido_id)
            if not itens:
                print("Pedido vazio.")
            else:
                cabecalhos = ["ID", "Livro", "Autor", "Preço", "Quantidade", "Categoria", "Fabricado em Mari"]
                print(tabulate(itens, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

        elif opcao == "4":
            print("\n-- Livros disponíveis --")
            livros = dao_livro.listar_todos()
            cabecalhos = ["ID", "Título", "Autor", "Preço", "Estoque"]
            print(tabulate(livros, headers=cabecalhos, tablefmt="fancy_grid", maxcolwidths=[5, 30, 20, 10, 8]))

        elif opcao == "0":
            break

        if opcao != "0":
            pausar()
            limpar_tela()

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


def ler_forma_pagamento():
    opcoes_validas = {"cartao", "boleto", "pix", "berries"}
    while True:
        forma = input("Forma de pagamento (cartao, boleto, pix, berries): ").strip().lower()
        if forma in opcoes_validas:
            return forma
        print("Erro: forma de pagamento inválida.")


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
