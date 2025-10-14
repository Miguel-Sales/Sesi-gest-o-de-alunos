import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import os

# DataFrame principal
colunas = ["Nome", "Idade", "Curso", "Nota Final"]
dados = pd.DataFrame(columns=colunas)

# --- Funções do Sistema ---
def cadastrar():
    global dados
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    curso = entry_curso.get().strip()
    nota = entry_nota.get().strip()

    if not nome or not idade or not curso or not nota:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
        nota = float(nota)
    except ValueError:
        messagebox.showerror("Erro de tipo", "Idade deve ser número inteiro e nota deve ser número decimal.")
        return

    novo = pd.DataFrame([[nome, idade, curso, nota]], columns=colunas)
    dados = pd.concat([dados, novo], ignore_index=True)
    atualizar_tabela()
    limpar_campos()

def atualizar_tabela(df=None):
    for linha in tree.get_children():
        tree.delete(linha)

    if df is None:
        df = dados

    for i, row in df.iterrows():
        tree.insert("", "end", values=list(row))

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_curso.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

def filtrar_notas():
    if dados.empty:
        messagebox.showinfo("Sem dados", "Nenhum aluno cadastrado.")
        return

    try:
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma média válida.")
        return

    filtrado = dados[dados["Nota Final"] > media]
    atualizar_tabela(filtrado)

def salvar_csv():
    if dados.empty:
        messagebox.showinfo("Aviso", "Nenhum dado para salvar.")
        return

    caminho = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("Arquivos CSV", "*.csv")],
                                           title="Salvar arquivo CSV")
    if caminho:
        dados.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", f"Dados salvos em:\n{caminho}")

def carregar_csv():
    global dados
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if not caminho:
        return

    try:
        dados = pd.read_csv(caminho)
        atualizar_tabela()
        messagebox.showinfo("Sucesso", f"Arquivo carregado:\n{os.path.basename(caminho)}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar arquivo:\n{e}")

def exportar_filtrado():
    if dados.empty:
        messagebox.showinfo("Sem dados", "Nenhum aluno cadastrado.")
        return

    try:
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma média válida.")
        return

    filtrado = dados[dados["Nota Final"] > media]

    if filtrado.empty:
        messagebox.showinfo("Sem resultados", "Nenhum aluno com nota acima da média informada.")
        return

    caminho = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("Arquivos CSV", "*.csv")],
                                           title="Exportar relatório filtrado")
    if caminho:
        filtrado.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", f"Relatório exportado para:\n{caminho}")

# --- Interface Tkinter ---
janela = tk.Tk()
janela.title("Sistema de Cadastro e Relatórios de Alunos")
janela.geometry("800x600")
janela.configure(bg="#f5f5f5")

# Frame de Cadastro
frame_cadastro = tk.LabelFrame(janela, text="Cadastro de Aluno", bg="#f5f5f5", padx=10, pady=10)
frame_cadastro.pack(fill="x", padx=10, pady=10)

tk.Label(frame_cadastro, text="Nome:", bg="#f5f5f5").grid(row=0, column=0, sticky="e")
entry_nome = tk.Entry(frame_cadastro, width=25)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_cadastro, text="Idade:", bg="#f5f5f5").grid(row=0, column=2, sticky="e")
entry_idade = tk.Entry(frame_cadastro, width=10)
entry_idade.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_cadastro, text="Curso:", bg="#f5f5f5").grid(row=1, column=0, sticky="e")
entry_curso = tk.Entry(frame_cadastro, width=25)
entry_curso.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_cadastro, text="Nota Final:", bg="#f5f5f5").grid(row=1, column=2, sticky="e")
entry_nota = tk.Entry(frame_cadastro, width=10)
entry_nota.grid(row=1, column=3, padx=5, pady=5)

btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", bg="#0078d7", fg="white", command=cadastrar)
btn_cadastrar.grid(row=2, column=0, columnspan=4, pady=10)

# Frame da Tabela
frame_tabela = tk.LabelFrame(janela, text="Tabela de Alunos", bg="#f5f5f5", padx=10, pady=10)
frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)

tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill="both", expand=True)

# Frame de Filtros e Arquivos
frame_funcoes = tk.LabelFrame(janela, text="Funções", bg="#f5f5f5", padx=10, pady=10)
frame_funcoes.pack(fill="x", padx=10, pady=10)

tk.Label(frame_funcoes, text="Filtrar nota acima de:", bg="#f5f5f5").grid(row=0, column=0)
entry_media = tk.Entry(frame_funcoes, width=10)
entry_media.grid(row=0, column=1, padx=5)

btn_filtrar = tk.Button(frame_funcoes, text="Filtrar", bg="#28a745", fg="white", command=filtrar_notas)
btn_filtrar.grid(row=0, column=2, padx=5)

btn_exportar = tk.Button(frame_funcoes, text="Exportar Filtrado", bg="#ffc107", command=exportar_filtrado)
btn_exportar.grid(row=0, column=3, padx=5)

btn_salvar = tk.Button(frame_funcoes, text="Salvar CSV", bg="#0078d7", fg="white", command=salvar_csv)
btn_salvar.grid(row=0, column=4, padx=5)

btn_carregar = tk.Button(frame_funcoes, text="Carregar CSV", bg="#6c757d", fg="white", command=carregar_csv)
btn_carregar.grid(row=0, column=5, padx=5)

janela.mainloop()
