import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.data_access_objects.livroDAO import LivroDAO
from app.data_access_objects.clienteDAO import ClienteDAO
from app.data_access_objects.funcionarioDAO import FuncionarioDAO
from app.data_access_objects.pedidoDAO import PedidoDAO
from app.data_access_objects.pedidoItemDAO import PedidoItemDAO
from app.data_access_objects.relatorioDAO import RelatorioDAO
from app.modelo import Livro, Cliente, Funcionario, Pedido, PedidoItem
from decimal import Decimal

class TestLivraria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configuração inicial para todos os testes. Limpa o BD e insere dados de teste."""
        print("Limpando e configurando dados de teste...")
        cls.livro_dao = LivroDAO()
        cls.cliente_dao = ClienteDAO()
        cls.funcionario_dao = FuncionarioDAO()
        cls.pedido_dao = PedidoDAO()
        cls.pedido_item_dao = PedidoItemDAO()
        cls.relatorio_dao = RelatorioDAO()

        # Limpeza completa para garantir um ambiente limpo
        con = cls.livro_dao.conectar()
        cursor = con.cursor()
        cursor.execute("TRUNCATE TABLE cliente, funcionario, fornecedor, livro, pedido, pedido_item RESTART IDENTITY CASCADE")
        con.commit()
        
        # Inserir dados de teste
        cls.funcionario_dao.inserir(Funcionario(id=None, nome="Vendedor Teste", cargo="Vendedor", email="vendedor@teste.com", ativo=True))
        cls.cliente_dao.inserir(Cliente(id=None, nome="Cliente Teste", email="cliente@teste.com", ativo=True))
        
        cls.livro_dao.inserir(Livro(id=None, titulo="Livro de Categoria A", autor="Autor A", preco=50.0, estoque=10, ativo=True))
        cls.livro_dao.inserir(Livro(id=None, titulo="Livro de Categoria B", autor="Autor B", preco=120.0, estoque=4, ativo=True)) # Estoque baixo
        cls.livro_dao.inserir(Livro(id=None, titulo="Livro Fabricado em Mari", autor="Autor C", preco=75.0, estoque=20, ativo=True))
        
        # Atualizar livros com categoria e fabricação
        cursor.execute("UPDATE livro SET categoria='Categoria A' WHERE titulo='Livro de Categoria A'")
        cursor.execute("UPDATE livro SET categoria='Categoria B' WHERE titulo='Livro de Categoria B'")
        cursor.execute("UPDATE livro SET categoria='Categoria C', fabricado_em_mari=True WHERE titulo='Livro Fabricado em Mari'")
        con.commit()
        cursor.close()
        con.close()


    @classmethod
    def tearDownClass(cls):
        """Limpeza após todos os testes. Remove todos os dados."""
        print("\nLimpando dados de teste...")
        con = cls.livro_dao.conectar()
        cursor = con.cursor()
        cursor.execute("TRUNCATE TABLE cliente, funcionario, fornecedor, livro, pedido, pedido_item RESTART IDENTITY CASCADE")
        con.commit()
        cursor.close()
        con.close()

    def test_01_filtros_livros(self):
        print("\nExecutando test_01_filtros_livros...")
        # Teste de busca por nome
        resultado = self.livro_dao.buscar_por_nome("Categoria A")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Livro de Categoria A")

        # Teste de busca por categoria
        resultado = self.livro_dao.buscar_por_categoria("Categoria B")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Livro de Categoria B")

        # Teste de busca por faixa de preço
        resultado = self.livro_dao.buscar_por_preco(40.0, 60.0)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Livro de Categoria A")

        # Teste de busca por fabricado em Mari
        resultado = self.livro_dao.buscar_fabricado_em_mari()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Livro Fabricado em Mari")
        print("test_01_filtros_livros: SUCESSO")

    def test_02_relatorio_estoque_baixo(self):
        print("\nExecutando test_02_relatorio_estoque_baixo...")
        resultado = self.livro_dao.listar_pouco_estoque()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], "Livro de Categoria B") # Título do livro com estoque 4
        self.assertEqual(resultado[0][3], 4) # Quantidade em estoque
        print("test_02_relatorio_estoque_baixo: SUCESSO")

    def test_03_fluxo_de_venda_e_relatorio(self):
        print("\nExecutando test_03_fluxo_de_venda_e_relatorio...")
        # Buscar IDs necessários
        cliente = self.cliente_dao.buscar_nome("Cliente Teste")[0]
        vendedor = self.funcionario_dao.listar_todos()[0] # Assume que só tem 1
        livro = self.livro_dao.buscar_por_nome("Categoria A")[0]
        
        cliente_id = cliente[0]
        vendedor_id = vendedor[0]
        livro_id = livro[0]
        estoque_inicial = livro[4]

        # 1. Criar um pedido
        pedido = Pedido(id=None, cliente_id=cliente_id, funcionario_id=vendedor_id, data=None, estado="EM_ANDAMENTO", valor=0.0, pago=False, forma_pagamento="berries", desconto=0.1)
        self.pedido_dao.inserir(pedido)
        pedido_id = self.pedido_dao.id_ultimo_pedido()
        self.assertIsNotNone(pedido_id)

        # 2. Adicionar item ao pedido
        item = PedidoItem(id=None, pedido_id=pedido_id, livro_id=livro_id, quantidade=2)
        self.pedido_item_dao.inserir(item)

        # ATUALIZAR O VALOR DO PEDIDO APÓS ADICIONAR ITEM
        self.pedido_dao.atualizar_valor(pedido_id)

        # 3. Verificar se o estoque foi atualizado
        livro_atualizado = self.livro_dao.buscar_id(livro_id)
        self.assertEqual(livro_atualizado[4], estoque_inicial - 2)

        # 4. Verificar valor total do pedido (com desconto)
        pedido_atualizado = self.pedido_dao.buscar_id(pedido_id)
        valor_esperado = (livro[3] * 2) * Decimal('0.9') # preco * quantidade * (1 - desconto)
        self.assertAlmostEqual(float(pedido_atualizado[4]), float(valor_esperado), places=2)

        # 5. Testar relatório de vendas
        # A data do pedido é CURRENT_TIMESTAMP, então usamos a data atual
        from datetime import datetime
        hoje = datetime.now()
        relatorio = self.relatorio_dao.gerar_relatorio_vendas_vendedor(hoje.month, hoje.year)
        
        self.assertEqual(len(relatorio), 1)
        self.assertEqual(relatorio[0][0], "Vendedor Teste") # Nome do vendedor
        self.assertEqual(relatorio[0][1], 1) # Total de vendas
        self.assertAlmostEqual(relatorio[0][2], valor_esperado) # Valor total vendido
        print("test_03_fluxo_de_venda_e_relatorio: SUCESSO")


if __name__ == "__main__":
    unittest.main(failfast=True, verbosity=2)
