from app.data_access_objects.baseDAO import BaseDAO

class RelatorioDAO(BaseDAO):
    def gerar_relatorio_vendas_vendedor(self, mes, ano):
        con = self.conectar()
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM sp_relatorio_vendas_vendedor(%s, %s)", (mes, ano))
            resultado = cursor.fetchall()
            return resultado
        finally:
            cursor.close()
            con.close()
