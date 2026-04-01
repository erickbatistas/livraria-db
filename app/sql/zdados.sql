-- Arquivo espelho de dados.sql para carga de dados de exemplo.

-- 1. CLIENTES
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

-- 2. FUNCIONARIOS
INSERT INTO funcionario (nome, cargo, email, ativo) VALUES
('Joao Silva', 'Vendedor', 'joao.silva@livraria.com', TRUE),
('Maria Oliveira', 'Gerente', 'maria.oliveira@livraria.com', TRUE),
('Pedro Santos', 'Caixa', 'pedro.santos@livraria.com', TRUE),
('Ana Souza', 'Vendedora', 'ana.souza@livraria.com', TRUE),
('Carlos Pereira', 'Estoquista', 'carlos.pereira@livraria.com', FALSE);

-- 3. FORNECEDORES
INSERT INTO fornecedor (nome, email, telefone, ativo) VALUES
('Editora Atlas', 'contato@atlas.com.br', '11-1111-1111', TRUE),
('Distribuidora Livros S.A.', 'vendas@distribuidoralivros.com', '21-2222-2222', TRUE),
('Papelaria Central', 'compras@papelariacentral.com', '31-3333-3333', TRUE),
('Importados & Cia', 'import@cia.com', '41-4444-4444', TRUE),
('Editora Moderna', 'contato@moderna.com.br', '51-5555-5555', FALSE);

-- 4. LIVROS
INSERT INTO livro (titulo, autor, preco, estoque, ativo, categoria, fabricado_em_mari) VALUES
('Dom Casmurro', 'Machado de Assis', 39.90, 15, TRUE, 'Classico', FALSE),
('1984', 'George Orwell', 45.00, 20, TRUE, 'Distopia', FALSE),
('A Hora da Estrela', 'Clarice Lispector', 29.90, 10, TRUE, 'Romance', FALSE),
('O Pequeno Principe', 'Antoine de Saint-Exupery', 25.00, 50, TRUE, 'Infantil', FALSE),
('O Senhor dos Aneis', 'J.R.R. Tolkien', 89.90, 8, TRUE, 'Fantasia', FALSE),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 59.90, 25, TRUE, 'Fantasia', FALSE),
('O Alquimista', 'Paulo Coelho', 35.00, 12, TRUE, 'Romance', TRUE),
('Cem Anos de Solidao', 'Gabriel Garcia Marquez', 55.00, 0, TRUE, 'Romance', FALSE),
('Sapiens', 'Yuval Noah Harari', 65.00, 18, TRUE, 'Historia', FALSE),
('It: A Coisa', 'Stephen King', 79.90, 7, TRUE, 'Terror', FALSE),
('Clean Code', 'Robert C. Martin', 95.00, 15, TRUE, 'Tecnologia', FALSE),
('O Codigo Da Vinci', 'Dan Brown', 42.00, 30, TRUE, 'Suspense', FALSE),
('Ensaio sobre a Cegueira', 'Jose Saramago', 48.00, 10, TRUE, 'Romance', FALSE),
('A Arte da Guerra', 'Sun Tzu', 19.90, 100, TRUE, 'Estrategia', TRUE),
('Design Patterns', 'GoF', 120.00, 5, TRUE, 'Tecnologia', FALSE);

-- 5. PEDIDOS
INSERT INTO pedido (cliente_id, funcionario_id, estado, valor, pago, status_confirmacao_pagamento, forma_pagamento, desconto) VALUES
(1, 1, 'ENTREGUE', 134.90, TRUE, 'CONFIRMADO', 'pix', 0),
(2, 4, 'EM_ANDAMENTO', 45.00, FALSE, 'PENDENTE', 'boleto', 0),
(3, 3, 'PRONTO', 120.00, TRUE, 'CONFIRMADO', 'cartao', 0),
(4, 4, 'ENTREGUE', 59.90, TRUE, 'CONFIRMADO', 'berries', 0.1),
(5, 4, 'EM_ANDAMENTO', 215.00, FALSE, 'PENDENTE', 'pix', 0),
(6, 1, 'PRONTO', 39.90, TRUE, 'CONFIRMADO', 'cartao', 0),
(1, 3, 'EM_ANDAMENTO', 95.00, FALSE, 'PENDENTE', 'berries', 0.1),
(8, 1, 'ENTREGUE', 19.90, TRUE, 'CONFIRMADO', 'pix', 0);

-- 6. ITENS DOS PEDIDOS
INSERT INTO pedido_item (pedido_id, livro_id, quantidade) VALUES
(1, 1, 1),
(1, 5, 1),
(2, 2, 1),
(3, 15, 1),
(4, 6, 1),
(5, 11, 2),
(5, 4, 1),
(6, 1, 1),
(7, 11, 1),
(8, 14, 1);