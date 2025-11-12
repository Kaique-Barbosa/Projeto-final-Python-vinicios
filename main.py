import customtkinter as ctk
import sqlite3 as db_sqlite3
from tkinter import messagebox

# Telas
from telas.cadastrar import cadastrar_livro
from telas.listar import listar_livros
from telas.atualizar import atualizar_livro
from telas.excluir import excluir_livro

# -------------------- CONFIGURAÇÕES --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- BANCO DE DADOS --------------------
conexao = db_sqlite3.connect("biblioteca.db")
cur = conexao.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS livro (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    data_publicacao TEXT NOT NULL,
    genero TEXT NOT NULL,
    qtd_livros INTEGER NOT NULL
)
""")
conexao.commit()

# -------------------- FUNÇÃO UTIL --------------------
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# -------------------- JANELA PRINCIPAL --------------------
app = ctk.CTk()
app.title("Sistema da Biblioteca")
centralizar_janela(app, 400, 480)

ctk.CTkLabel(app, text=" Gerenciamento de Livros", font=("Arial", 20)).pack(pady=15)

ctk.CTkButton(app, text="Cadastrar Livro", command=lambda: cadastrar_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Listar Livros", command=lambda: listar_livros(app, cur, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Atualizar Livro", command=lambda: atualizar_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Excluir Livro", command=lambda: excluir_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Sair", command=app.destroy).pack(pady=20)

app.mainloop()
conexao.close()
