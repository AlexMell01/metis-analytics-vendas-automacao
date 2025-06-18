import pandas as pd
import os

# Caminhos
pasta_entrada = "entrada"
pasta_saida = "data"
arquivo_saida = "vendas_transformado.csv"

# Garantir que as pastas existam
os.makedirs(pasta_entrada, exist_ok=True)
os.makedirs(pasta_saida, exist_ok=True)

# Listar arquivos suportados
arquivos = [f for f in os.listdir(pasta_entrada) if f.endswith((".csv", ".xlsx"))]

if not arquivos:
    print("⚠️ Nenhum arquivo CSV ou XLSX encontrado na pasta 'entrada'.")
    exit()

# Carregar arquivos
dfs = []
for arquivo in arquivos:
    caminho = os.path.join(pasta_entrada, arquivo)
    try:
        if arquivo.endswith(".csv"):
            df = pd.read_csv(caminho)
        elif arquivo.endswith(".xlsx"):
            df = pd.read_excel(caminho)
        dfs.append(df)
    except Exception as e:
        print(f"❌ Erro ao ler {arquivo}: {e}")

# Concatenar tudo
df = pd.concat(dfs, ignore_index=True)
print("🧾 Colunas encontradas:", df.columns.tolist())

# Mapeamento de meses para conversão
meses_map = {
    'Janeiro': 1, 'Fevereiro': 2, 'Março': 3,
    'Abril': 4, 'Maio': 5, 'Junho': 6,
    'Julho': 7, 'Agosto': 8, 'Setembro': 9,
    'Outubro': 10, 'Novembro': 11, 'Dezembro': 12
}

# Tentativa de transformação adaptada ao seu formato
try:
    # Converter a data e extrair o mês
    df['Data Pedido'] = pd.to_datetime(df['Data Pedido'], errors='coerce')
    df['Mês'] = df['Data Pedido'].dt.month.map({v: k for k, v in meses_map.items()})

    # Separar quantidade e preço unitário
    split = df['Qtde/Preco Unit'].str.split('/', expand=True)
    df['Quantidade Vendida'] = pd.to_numeric(split[0], errors='coerce')
    df['Preço Unitário'] = pd.to_numeric(split[1], errors='coerce')

    # Calcular receita
    df['Receita Total'] = df['Quantidade Vendida'] * df['Preço Unitário']

    # Usar código da loja como canal
    df['Canal'] = df['Código Loja']

    # Converter mês para número e criar data
    df['Mês_Num'] = df['Mês'].map(meses_map)
    df['Ano'] = 2025
    df['Data'] = pd.to_datetime(df.rename(columns={'Ano': 'year', 'Mês_Num': 'month'}).assign(day=1)[['year', 'month', 'day']])

    # Reorganizar colunas finais
    df = df[['Data', 'Mês', 'Canal', 'Produto', 'Quantidade Vendida', 'Preço Unitário', 'Receita Total']]
    df.to_csv(os.path.join(pasta_saida, arquivo_saida), index=False)
    print("✅ Arquivo transformado com sucesso:")
    print(df.head())

except Exception as e:
    print(f"❌ Erro na transformação dos dados: {e}")
