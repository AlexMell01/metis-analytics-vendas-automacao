import sqlite3
import os
import pandas as pd

# Caminho do banco de dados
caminho_db = os.path.join('data', 'vendas.db')

# Conectar ao banco
conn = sqlite3.connect(caminho_db)

# Função auxiliar para exibir resultados com pandas
def exibir_consulta(query, descricao):
    print(f"\n🟦 {descricao}")
    df = pd.read_sql_query(query, conn)
    print(df)

# Consulta 1: Receita total por canal
exibir_consulta("""
SELECT Canal, ROUND(SUM(Receita), 2) AS Receita_Total
FROM vendas
GROUP BY Canal
ORDER BY Receita_Total DESC
""", "Receita total por canal")

# Consulta 2: Produtos mais vendidos (quantidade)
exibir_consulta("""
SELECT Produto, SUM(Quantidade) AS Total_Vendido
FROM vendas
GROUP BY Produto
ORDER BY Total_Vendido DESC
""", "Produtos mais vendidos (por quantidade)")

# Consulta 3: Receita por mês (com ordenação cronológica)
exibir_consulta("""
SELECT strftime('%Y-%m', Data) AS Mes, ROUND(SUM(Receita), 2) AS Receita_Mensal
FROM vendas
GROUP BY Mes
ORDER BY Mes
""", "Receita total por mês")

# Fechar conexão
conn.close()
