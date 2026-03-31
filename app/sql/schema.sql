CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(50),
    ativo BOOLEAN DEFAULT TRUE
);


CREATE TYPE estado_pedido AS ENUM ('EM_ANDAMENTO', 'PRONTO', 'ENTREGUE'); -- FIX: Alterar para "ESPERANDO_PAGAMENTO", "ENVIADO", "ENTREGUE"?


CREATE TABLE livro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    preco DECIMAL(8, 2) NOT NULL,
    estoque INTEGER DEFAULT 0,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    fabricado_em_mari BOOLEAN DEFAULT FALSE
);

CREATE TABLE funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE fornecedor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    telefone VARCHAR(20),
    ativo BOOLEAN DEFAULT TRUE
);


CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    funcionario_id INTEGER NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado estado_pedido DEFAULT 'EM_ANDAMENTO',
    valor DECIMAL(10, 2) DEFAULT 0.00,
    pago BOOLEAN DEFAULT FALSE,
    ativo BOOLEAN DEFAULT TRUE,
    forma_pagamento VARCHAR(50),
    desconto REAL DEFAULT 0,
    
    -- Chave Estrangeira: impede criar pedido para cliente inexistente
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) 
        REFERENCES cliente(id) ON DELETE CASCADE,  -- Caso o cliente seja deletado, seus pedidos também serão
    CONSTRAINT fk_funcionario FOREIGN KEY (funcionario_id)
        REFERENCES funcionario(id)
);


CREATE TABLE pedido_item (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    
    CONSTRAINT fk_pedido FOREIGN KEY (pedido_id) 
        REFERENCES pedido(id) ON DELETE CASCADE,
    CONSTRAINT fk_livro FOREIGN KEY (livro_id) 
        REFERENCES livro(id) 
);

-- Índices para otimizar buscas
CREATE INDEX idx_cliente_nome ON cliente(nome);
CREATE INDEX idx_livro_titulo ON livro(titulo);
CREATE INDEX idx_livro_categoria ON livro(categoria);

-- View para livros com pouco estoque
CREATE VIEW vw_livros_pouco_estoque AS
SELECT id, titulo, autor, estoque
FROM livro
WHERE estoque < 5 AND ativo = TRUE;

-- Stored Procedure para relatório de vendas por vendedor
CREATE OR REPLACE FUNCTION sp_relatorio_vendas_vendedor(mes INT, ano INT)
RETURNS TABLE(vendedor_nome VARCHAR, total_vendas BIGINT, valor_total_vendido DECIMAL) AS $$
BEGIN
    RETURN QUERY
    SELECT
        f.nome AS vendedor_nome,
        COUNT(p.id) AS total_vendas,
        SUM(p.valor) AS valor_total_vendido
    FROM pedido p
    JOIN funcionario f ON p.funcionario_id = f.id
    WHERE EXTRACT(MONTH FROM p.data_pedido) = mes AND EXTRACT(YEAR FROM p.data_pedido) = ano
    GROUP BY f.nome
    ORDER BY total_vendas DESC;
END;
$$ LANGUAGE plpgsql;
