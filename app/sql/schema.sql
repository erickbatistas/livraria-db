CREATE TABLE livro (
    id SERIAL,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    preco DECIMAL(8, 2),
    estoque INTEGER,
    PRIMARY KEY (id)
)