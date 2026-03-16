# Sistema de Livraria

Este projeto foi desenvolvido para a disciplina de Banco de Dados I, ministrada por Marcelo Iury na UFPB.
A aplicação é um sistema de vendas de uma livraria.

## Configurações iniciais

A aplicação utiliza psql, uv e Docker.
Crie uma imagem no Docker com postgres:

```bash
sudo docker run --name <nome-do-container> -e POSTGRES_PASSWORD=<sua-senha> -p 5432:5432 -d postgres
```

Crie um Database no Postgres através do Docker:

```bash
sudo docker exec -it <nome-do-container> psql -U postgres -c "CREATE DATABASE <nome-do-database>;"
```

Inicialize o banco de dados com o schema.sql através do Docker e instale as dependências com o uv:

```bash
sudo docker exec -i <nome-do-container> psql -U postgres -d <nome-do-database> < app/sql/schema.sql

uv sync
```

Rode a aplicação:

```bash
uv run python app/main.py
```

## Modelagem — Diagrama UML de Classes

```mermaid
classDiagram
    direction TB

    class Cliente {
        +int id
        +str nome
        +str email
        +bool ativo
        +inserir()
        +alterar()
        +remover()
        +listar_todos()
        +buscar_id(id)
        +buscar_nome(nome)
        +gerar_relatorio()
    }

    class Database {
        +conectar()
    }

    class EstadoPedido {
        <<enumeration>>
        EM_ANDAMENTO
        PRONTO
        ENTREGUE
    }

    class Livro {
        +int id
        +str titulo
        +str autor
        +float preco
        +int estoque
        +bool ativo
        +inserir()
        +alterar()
        +remover()
        +listar_todos()
        +buscar_id(id)
        +gerar_relatorio()
        +atualizar_quantidade(delta)
    }

    class Pedido {
        +int id
        +int cliente_id
        +date data
        +EstadoPedido estado
        +float valor
        +bool pago
        +inserir()
        +alterar()
        +remover()
        +listar_todos()
        +listar_cliente(cliente_id)  
        +buscar_id(id)
        +pagar()
        +atualizar_estado(estado)
        +gerar_relatorio()
    }

    class PedidoItem {
        +int id
        +int pedido_id
        +int livro_id
        +int quantidade
        +inserir()
        +remover()
        +listar_pedido(pedido_id)
    }

    Cliente "1" --> "0..*" Pedido : realiza
    Pedido "1" --> "1..*" PedidoItem : contém
    PedidoItem "0..*" --> "1" Livro : referencia
    Pedido --> "1" EstadoPedido : estado
    Cliente ..> Database : usa
    Pedido ..> Database : usa
    Livro ..> Database : usa
```
