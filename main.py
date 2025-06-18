import os

print("🚀 Iniciando execução do pipeline Metis Analytics...")

# Executar scripts em sequência
try:
    os.system("python etl.py")
    os.system("python load_db.py")
    os.system("python gerar_relatorio.py")
    os.system("python enviar_email.py")
    print("✅ Pipeline executado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao executar o pipeline: {e}")
