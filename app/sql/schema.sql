CREATE TABLE livro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    preco DECIMAL(8, 2),
    estoque INTEGER DEFAULT 0,
    ativo BOOLEAN DEFAULT TRUE
)

CREATE TYPE estado_pedido AS ENUM ('EM_ANDAMENTO', 'PRONTO', 'ENTREGUE');


CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    numero VARCHAR(20), -- telefone ou documento
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado estado_pedido DEFAULT 'EM_ANDAMENTO',
    valor_total DECIMAL(10, 2) DEFAULT 0.00,
    pago BOOLEAN DEFAULT FALSE,
    
    -- Chave Estrangeira: impede criar pedido para cliente inexistente
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) 
        REFERENCES cliente(id) ON DELETE CASCADE  --caso o cliente seja deletado, seus pedidos também serão
);

-- 5. Tabela PedidoItem (Tabela de ligação entre Pedido e Livro)
CREATE TABLE pedido_item (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    livro_id INTEGER NOT NULL, -- "item_id" no seu diagrama
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    
    CONSTRAINT fk_pedido FOREIGN KEY (pedido_id) 
        REFERENCES pedido(id) ON DELETE CASCADE,
    CONSTRAINT fk_livro FOREIGN KEY (livro_id) 
        REFERENCES livro(id) 
);