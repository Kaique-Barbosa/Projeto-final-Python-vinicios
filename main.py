import customtkinter as ctk
import sqlite3 as db_sqlite3
from tkinter import messagebox

# Telas
from telas.cadastrar import cadastrar_livro
from telas.listar import listar_livros
from telas.atualizar import atualizar_livro
from telas.excluir import excluir_livro

# -------------------- CONFIGURAÇÕES  DE TEMAS DO CUMTOMCTK--------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- AREA DO BANCO DE DADOS --------------------
conexao = db_sqlite3.connect("biblioteca.db")
cur = conexao.cursor()

# CODIGO SQL PARA CRIAR A TABELA LIVRO CASO ELA NÃO EXISTA
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

# ------- FUNÇÃO PARA OBTER A LARGURA E ALTURA MONITOR E DEFINIR O TAMANHO DAS JANELAS --------------------
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


# -------------------- JANELA PRINCIPAL --------------------
#  ESSA JANELA CONTEM O MENU INICIAL DO SISTEMA
app = ctk.CTk()
app.title("Sistema da Biblioteca")
centralizar_janela(app, 400, 480)  #APP É A INSTANCIA DO CTK, 400 É A LARGURA E 480 A ALTURA

#  ABAIXO ESTÃO OS BOTOES CHAMANDO AS FUNÇÕES DAS TELAS
ctk.CTkLabel(app, text=" Gerenciamento de Livros", font=("Arial", 20)).pack(pady=15)

#  AQUI CADA BOTÃO ENTÁ CHAMANDO UMA FUNÇÃO LABDDA DA SUA RESPECTIVA TELA, PASSANDO OS PARÂMETROS :
#  app: A INSTANCIA DO CTK, cur: O CURSOR DO BANCO DE DADOS, conexao: A CONEXÃO DO BANCO DE DADOS, centralizar_janela: A FUNÇÃO PARA CENTRALIZAR A JANELA

ctk.CTkButton(app, text="Cadastrar Livro", command=lambda: cadastrar_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Listar Livros", command=lambda: listar_livros(app, cur, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Atualizar Livro", command=lambda: atualizar_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Excluir Livro", command=lambda: excluir_livro(app, cur, conexao, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Sair", command=app.destroy).pack(pady=20)

app.mainloop()
conexao.close()
