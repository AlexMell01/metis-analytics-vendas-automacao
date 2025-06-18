import schedule
import time
import os

# Caminhos dos scripts
def executar_pipeline():
    print("⏳ Iniciando execução do pipeline Metis Analytics...")
    os.system("python etl.py")
    os.system("python load_db.py")
    os.system("python gerar_relatorio.py")
    os.system("python enviar_email.py")
    print("✅ Pipeline executado com sucesso!")

# Agendamento: todos os dias às 08h00
schedule.every().day.at("08:00").do(executar_pipeline)

print("⏰ Agendamento ativado: o pipeline será executado todos os dias às 08:00.")

# Loop infinito para manter o agendador rodando
while True:
    schedule.run_pending()
    time.sleep(60)
