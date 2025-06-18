📊 Metis Analytics – Pipeline de Vendas Automatizado
Este projeto representa um pipeline completo de automação para dados de vendas. Ele realiza coleta de arquivos, tratamento (ETL), análise, geração de relatórios em PDF com visual profissional, e envio automático por e-mail. Tudo isso com interface gráfica (GUI) e executável .exe.

🚀 Funcionalidades
✅ Coleta automática de arquivos .csv ou .xlsx
✅ Transformação e limpeza de dados
✅ Armazenamento em banco SQLite
✅ Geração de gráficos (barras e linha)
✅ Relatório em PDF com logo Metis
✅ Envio automático por e-mail com anexo
✅ Interface gráfica amigável (GUI)
✅ Versão .exe para execução com dois cliques

🛠 Tecnologias usadas
Python 3.13

Pandas

Matplotlib

ReportLab

SQLite

Tkinter (GUI)

PyInstaller

Schedule

SMTP (e-mail automático)

📁 Estrutura do Projeto
projeto_etl_vendas/
├── app_gui.py # Interface visual
├── etl.py # Coleta e transformação de dados
├── load_db.py # Carga no banco SQLite
├── gerar_relatorio.py # Gráficos e PDF
├── enviar_email.py # Envio automático por e-mail
├── entrada/ # Arquivos de entrada (.csv/.xlsx)
├── data/ # Saídas: .db, .csv, .pdf
└── dist/metis_gui.exe # Versão empacotada (opcional)

📷 Demonstrações (adicione depois)
Exemplo do PDF: ./data/relatorio_vendas.pdf
Interface GUI: ./screenshots/gui_metis.png

▶️ Como executar
Clone o repositório:
git clone https://github.com/AlexMell01/metis-analytics-vendas-automacao.git

Instale as dependências:
pip install -r requirements.txt

Execute o app:
python app_gui.py

Ou use o executável:
dist/metis_gui.exe

📩 Contato
Desenvolvido por Alex Costa
LinkedIn: https://linkedin.com/in/alexmell01

🏷️ Licença
MIT © 2025 – Metis Analytics