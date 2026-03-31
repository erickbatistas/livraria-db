-- 1. CLIENTES (10 Exemplos)
INSERT INTO cliente (nome, email, ativo) VALUES 
('Erick Batista', 'erick@email.com', TRUE),
('Ana Silva', 'ana.silva@email.com', TRUE),
('Lucas Oliveira', 'lucas.dev@outlook.com', TRUE),
('Beatriz Souza', 'bea@empresa.com.br', TRUE),
('Carlos Mendes', 'carlos.mendes@gmail.com', TRUE),
('Mariana Costa', 'mari.costa@yahoo.com', TRUE),
('Ricardo Alves', 'ricardo.alves@bol.com.br', FALSE),
('Fernanda Lima', 'fer.lima@gmail.com', TRUE),
('Roberto Junior', 'roberto.jr@hotmail.com', TRUE),
('Juliana Paes', 'ju.paes@gmail.com', TRUE);

-- 2. LIVROS (15 Exemplos de diversos gêneros)
INSERT INTO livro (titulo, autor, preco, estoque, ativo) VALUES 
('Dom Casmurro', 'Machado de Assis', 39.90, 15, TRUE),
('1984', 'George Orwell', 45.00, 20, TRUE),
('A Hora da Estrela', 'Clarice Lispector', 29.90, 10, TRUE),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 25.00, 50, TRUE),
('O Senhor dos Anéis', 'J.R.R. Tolkien', 89.90, 8, TRUE),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 59.90, 25, TRUE),
('O Alquimista', 'Paulo Coelho', 35.00, 12, TRUE),
('Cem Anos de Solidão', 'Gabriel García Márquez', 55.00, 0, TRUE), -- Esgotado
('Sapiens', 'Yuval Noah Harari', 65.00, 18, TRUE),
('It: A Coisa', 'Stephen King', 79.90, 7, TRUE),
('Clean Code', 'Robert C. Martin', 95.00, 15, TRUE),
('O Código Da Vinci', 'Dan Brown', 42.00, 30, TRUE),
('Ensaio sobre a Cegueira', 'José Saramago', 48.00, 10, TRUE),
('A Arte da Guerra', 'Sun Tzu', 19.90, 100, TRUE),
('Design Patterns', 'GoF', 120.00, 5, TRUE);

-- 3. PEDIDOS (Simulando fluxo de caixa e estados)
INSERT INTO pedido (cliente_id, estado, valor, pago) VALUES 
(1, 'ENTREGUE', 134.90, TRUE),
(2, 'EM_ANDAMENTO', 45.00, FALSE),
(3, 'PRONTO', 120.00, TRUE),
(4, 'ENTREGUE', 59.90, TRUE),
(5, 'EM_ANDAMENTO', 215.00, FALSE),
(6, 'PRONTO', 39.90, TRUE),
(1, 'EM_ANDAMENTO', 95.00, FALSE), -- Segundo pedido do Erick
(8, 'ENTREGUE', 19.90, TRUE);

-- 4. ITENS DO PEDIDO (Relacionando múltiplos livros por pedido)
INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES 
-- Pedido 1 (Erick)
(1, 1, 1), (1, 5, 1), 
-- Pedido 2 (Ana)
(2, 2, 1),
-- Pedido 3 (Lucas)
(3, 15, 1),
-- Pedido 4 (Beatriz)
(4, 6, 1),
-- Pedido 5 (Carlos)
(5, 11, 2), (5, 4, 1),
-- Pedido 6 (Mariana)
(6, 1, 1),
-- Pedido 7 (Erick de novo)
(7, 11, 1),
-- Pedido 8 (Fernanda)
(8, 14, 1);

-- 5. FUNCIONÁRIOS (5 Exemplos)
INSERT INTO funcionario (nome, cargo, email, ativo) VALUES
('João Silva', 'Vendedor', 'joao.silva@livraria.com', TRUE),
('Maria Oliveira', 'Gerente', 'maria.oliveira@livraria.com', TRUE),
('Pedro Santos', 'Caixa', 'pedro.santos@livraria.com', TRUE),
('Ana Souza', 'Vendedora', 'ana.souza@livraria.com', TRUE),
('Carlos Pereira', 'Estoquista', 'carlos.pereira@livraria.com', FALSE);

-- 6. FORNECEDORES (5 Exemplos)
INSERT INTO fornecedor (nome, email, telefone, ativo) VALUES
('Editora Atlas', 'contato@atlas.com.br', '11-1111-1111', TRUE),
('Distribuidora Livros S.A.', 'vendas@distribuidoralivros.com', '21-2222-2222', TRUE),
('Papelaria Central', 'compras@papelariacentral.com', '31-3333-3333', TRUE),
('Importados & Cia', 'import@cia.com', '41-4444-4444', TRUE),
('Editora Moderna', 'contato@moderna.com.br', '51-5555-5555', FALSE);

-- Atualizando pedidos para associar a funcionários
UPDATE pedido SET funcionario_id = 1 WHERE id IN (1, 6, 8);
UPDATE pedido SET funcionario_id = 4 WHERE id IN (2, 4, 5);
UPDATE pedido SET funcionario_id = 3 WHERE id IN (3, 7);