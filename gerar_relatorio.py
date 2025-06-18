import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os

# === Consulta SQL ===
conn = sqlite3.connect(os.path.join("data", "vendas.db"))

df_canal = pd.read_sql_query("""
SELECT Canal, ROUND(SUM(Receita), 2) AS Receita_Total
FROM vendas
GROUP BY Canal
ORDER BY Receita_Total DESC
""", conn)

df_mes = pd.read_sql_query("""
SELECT strftime('%Y-%m', Data) AS Mes, ROUND(SUM(Receita), 2) AS Receita_Mensal
FROM vendas
GROUP BY Mes
ORDER BY Mes
""", conn)

df_produto = pd.read_sql_query("""
SELECT Produto, SUM(Quantidade) AS Total_Vendido
FROM vendas
GROUP BY Produto
ORDER BY Total_Vendido DESC
""", conn)

conn.close()

# === Gerar gráficos ===
def salvar_grafico(df, titulo, x_col, y_col, nome_arquivo, tipo='bar', cor='steelblue'):
    plt.figure(figsize=(8, 5))
    if tipo == 'bar':
        df.plot(kind='bar', x=x_col, y=y_col, legend=False, color=cor)
    elif tipo == 'line':
        df.plot(kind='line', x=x_col, y=y_col, marker='o', color=cor, legend=False)
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(nome_arquivo)
    plt.close()

salvar_grafico(df_canal, "Receita Total por Canal", "Canal", "Receita_Total", "grafico_canal.png")
salvar_grafico(df_mes, "Receita por Mês", "Mes", "Receita_Mensal", "grafico_mes.png", tipo='line', cor='green')
salvar_grafico(df_produto, "Produtos Mais Vendidos", "Produto", "Total_Vendido", "grafico_produto.png", cor='darkorange')

# === Criar PDF ===
pdf_path = os.path.join("data", "relatorio_vendas.pdf")
c = canvas.Canvas(pdf_path, pagesize=A4)
largura, altura = A4
logo_path = "logo_metis.png"

def nova_pagina(titulo, imagem):
    if os.path.exists(logo_path):
        c.drawImage(ImageReader(logo_path), 50, altura - 100, width=100, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 16)
    c.drawString(160, altura - 70, "Metis Analytics – Relatório de Vendas")
    c.setFont("Helvetica", 13)
    c.drawString(50, altura - 120, titulo)
    c.drawImage(imagem, 50, altura - 550, width=500, preserveAspectRatio=True, mask='auto')

    # Rodapé
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 30, f"Gerado em {datetime.today().strftime('%d/%m/%Y %H:%M')} – Metis Analytics")
    c.showPage()

# Páginas
nova_pagina("📊 Receita Total por Canal", "grafico_canal.png")
nova_pagina("📈 Receita Mensal", "grafico_mes.png")
nova_pagina("📦 Produtos Mais Vendidos", "grafico_produto.png")

c.save()

print("✅ Relatório PDF premium gerado com sucesso.")
