import smtplib
from email.message import EmailMessage
import os

# === CONFIGURAÇÕES DO E-MAIL ===
EMAIL_REMETENTE = "alexasc.automacao@gmail.com"
SENHA_APP = "yefh rfda xrzq gexy"
EMAIL_DESTINATARIO = "mellfuture@gmail.com"

# Caminho do arquivo PDF
caminho_pdf = os.path.join("data", "relatorio_vendas.pdf")

# Criar o e-mail
msg = EmailMessage()
msg['Subject'] = "📊 Relatório Automático de Vendas"
msg['From'] = EMAIL_REMETENTE
msg['To'] = EMAIL_DESTINATARIO
msg.set_content("Segue em anexo o relatório de vendas gerado automaticamente pelo pipeline Metis Analytics.")

# Adicionar anexo PDF
with open(caminho_pdf, 'rb') as f:
    pdf_data = f.read()
    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='relatorio_vendas.pdf')

# Enviar via servidor SMTP
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, SENHA_APP)
        smtp.send_message(msg)
        print("✅ E-mail enviado com sucesso!")
except Exception as e:
    print("❌ Erro ao enviar e-mail:", e)
