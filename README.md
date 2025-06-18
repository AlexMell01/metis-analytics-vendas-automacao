# 📊 Metis Analytics – Pipeline Automatizado de Vendas

Este projeto executa uma automação completa de dados de vendas. Ele coleta arquivos, trata e transforma os dados (ETL), armazena no banco, gera gráficos e relatórios PDF visuais e envia tudo automaticamente por e-mail — com interface gráfica ou via `.exe`.

---

## 🔍 Visão Geral

- Processamento de arquivos `.csv` e `.xlsx` de vendas com estrutura variada.
- Transformação automatizada para gerar colunas padrão e consolidação no banco.
- Geração automática de gráficos e relatório PDF com marca visual.
- Envio do PDF final por e-mail e interface gráfica com execução automática.

---

## 📊 Análises Realizadas

- Receita total por canal de venda
- Produtos mais vendidos por quantidade
- Receita mensal consolidada (timeline)
- Gráficos de barra e linha gerados via matplotlib
- PDF estruturado com logotipo e rodapé profissional

---

## 🧱 Estrutura do Projeto

```
projeto_etl_vendas/
├── app_gui.py            # Interface visual
├── etl.py                # Coleta e transformação dos dados
├── load_db.py            # Inserção no banco SQLite
├── gerar_relatorio.py    # Geração de gráficos e PDF
├── enviar_email.py       # Envio automático do PDF por e-mail
├── entrada/              # Pasta onde os arquivos originais são colocados
├── data/                 # Arquivos gerados (.csv, .db, .pdf)
└── dist/metis_gui.exe    # Versão empacotada com interface
```

---

## ▶️ Como Executar

1. Clone o repositório:  
`git clone https://github.com/AlexMell01/metis-analytics-vendas-automacao.git`

2. Instale as dependências:  
`pip install -r requirements.txt`

3. Rode com interface:
`python app_gui.py`  
ou execute `dist/metis_gui.exe`

---

## 📩 Contato

Desenvolvido por **Alex Costa**  
🔗 LinkedIn: [linkedin.com/in/alexmell01](https://linkedin.com/in/alexmell01)

---

## 🏷️ Licença

MIT © 2025 – Metis Analytics