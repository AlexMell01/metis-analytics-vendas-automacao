import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

# Função principal
def executar_pipeline():
    if not caminho_arquivo.get():
        messagebox.showwarning("Aviso", "Selecione um arquivo antes de executar.")
        return

    try:
        # Criar pasta entrada se não existir
        os.makedirs("entrada", exist_ok=True)

        # Copiar o arquivo selecionado para a pasta entrada
        destino = os.path.join("entrada", os.path.basename(caminho_arquivo.get()))
        if not os.path.exists(destino):
            shutil.copy(caminho_arquivo.get(), destino)


        # Executar o pipeline
        os.system("python etl.py")
        os.system("python load_db.py")
        os.system("python gerar_relatorio.py")
        os.system("python enviar_email.py")

        messagebox.showinfo("Sucesso", "Pipeline executado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar: {e}")

# Selecionar arquivo
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Planilhas", "*.csv *.xlsx")])
    caminho_arquivo.set(arquivo)

# Interface
janela = tk.Tk()
janela.title("Metis Analytics")
janela.geometry("400x200")

caminho_arquivo = tk.StringVar()

tk.Label(janela, text="Selecione o arquivo de vendas:", font=("Arial", 12)).pack(pady=10)
tk.Entry(janela, textvariable=caminho_arquivo, width=40).pack(pady=5)
tk.Button(janela, text="Procurar", command=selecionar_arquivo).pack(pady=5)
tk.Button(janela, text="Executar pipeline", command=executar_pipeline, bg="#003366", fg="white", font=("Arial", 10)).pack(pady=15)

janela.mainloop()
