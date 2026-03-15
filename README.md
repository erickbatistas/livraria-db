# Sistema de Livraria

Este projeto foi desenvolvido para a disciplina de Banco de Dados I, ministrada por Marcelo Iury na UFPB.
A aplicação é um sistema de vendas de uma livraria.

## Configurações iniciais

A aplicação utiliza psql, uv e Docker.
Crie um Database no Postgres através do Docker:

```bash
sudo docker exec -it meu-postgres psql -U postgres

# Executar comando no docker
postgres#= CREATE DATABASE livraria-db

# Sair
postgres#= \q
```

Inicialize o banco de dados com o schema.sql através do Docker e instale as dependências com o uv:

```bash
sudo docker exec -i meu-postgres psql -U postgres -d livraria_testes < app/sql/schema.sql

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
        +str numero
        +bool ativo
        +inserir()
        +alterar()
        +remover()
        +buscar_por_nome(nome) List
        +listar_todos() List
        +exibir(id)
        +gerar_relatorio()
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
        +buscar(id)
        +listar_todos() List
        +listar_por_cliente(cliente_id) List
        +exibir(id)
        +gerar_relatorio()
        +atualizar_estado(estado)
        +marcar_pago()
    }

    class PedidoItem {
        +int id
        +int pedido_id
        +int item_id
        +int quantidade
        +inserir()
        +remover()
        +listar_por_pedido(pedido_id) List
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
        +listar_todos() List
        +exibir(id)
        +gerar_relatorio()
        +atualizar_quantidade(delta)
    }

    class EstadoPedido {
        <<enumeration>>
        EM_ANDAMENTO
        PRONTO
        ENTREGUE
    }

    class Database {
        +conectar()
        +fechar()
    }

    Cliente "1" --> "1..*" Pedido : realiza
    Pedido "1" --> "1..*" PedidoItem : contém
    PedidoItem "0..*" --> "1" Livro : referencia
    Pedido --> "1" EstadoPedido : estado
    Cliente ..> Database : usa
    Pedido ..> Database : usa
    Livro ..> Database : usa
```
