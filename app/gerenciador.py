from database import conectar

class LivroDAO:
    def inserir(self, livro):
        con = conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO livro (titulo, autor, preco, estoque) VALUES (%s, %s, %s, %s)", 
                       (livro.titulo, livro.autor, livro.preco, livro.estoque))
        con.commit() # Salva no banco
        cursor.close()
        con.close()

    def listar_todos(self):
        # Aqui você faria o SELECT * FROM livros
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT id, titulo, autor, preco, estoque FROM livro")
        resultado = cursor.fetchall()
        print("Id   Título      Autor       Preço   Estoque")
        for i in range(len(resultado)):
            print(f"{resultado[i][0]}   {resultado[i][1]}       {resultado[i][2]}       {resultado[i][3]}   {resultado[i][4]}")
        cursor.close()
        con.close()

    def gerar_relatorio(self):
        # Requisito 6: Exibir quantidade de elementos e valor total 
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT COUNT(*), SUM(preco * estoque) FROM livro")
        resultado = cursor.fetchone()
        print(f"Total de livros: {resultado[0]}")
        print(f"Valor total em estoque: R$ {resultado[1]}")
        cursor.close()
        con.close()