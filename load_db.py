import pandas as pd
import sqlite3
import os

# Caminhos
caminho_csv = os.path.join("data", "vendas_transformado.csv")
caminho_db = os.path.join("data", "vendas.db")

# Carregar dados transformados
df = pd.read_csv(caminho_csv)

# Conectar ao banco
conn = sqlite3.connect(caminho_db)
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    Data TEXT,
    Mês TEXT,
    Canal TEXT,
    Produto TEXT,
    Quantidade INTEGER,
    Preco REAL,
    Receita REAL
)
""")

# Limpar tabela anterior
cursor.execute("DELETE FROM vendas")

# Inserir dados com validação contra NaN
for _, row in df.iterrows():
    if pd.notnull(row['Quantidade Vendida']) and pd.notnull(row['Preço Unitário']) and pd.notnull(row['Receita Total']):
        cursor.execute("""
            INSERT INTO vendas (Data, Mês, Canal, Produto, Quantidade, Preco, Receita)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row['Data'],
            row['Mês'],
            row['Canal'],
            row['Produto'],
            int(row['Quantidade Vendida']),
            float(row['Preço Unitário']),
            float(row['Receita Total'])
        ))

# Salvar e fechar
conn.commit()
conn.close()

print("✅ Dados carregados no banco com sucesso!")
