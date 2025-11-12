import customtkinter as ctk
from tkinter import messagebox

def cadastrar_livro(app, cur, conexao, centralizar):
    def salvar():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        data_publicacao = entry_data.get()
        genero = entry_genero.get()
        qtd_livros = entry_qtd.get()

        if not titulo or not autor or not data_publicacao or not genero or not qtd_livros:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        cur.execute(
            "INSERT INTO livro (titulo, autor, data_publicacao, genero, qtd_livros) VALUES (?, ?, ?, ?, ?)",
            (titulo, autor, data_publicacao, genero, int(qtd_livros))
        )
        conexao.commit()
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        janela_cadastro.destroy()

    janela_cadastro = ctk.CTkToplevel(app)
    janela_cadastro.title("Cadastrar Livro")
    centralizar(janela_cadastro, 320, 400)
    janela_cadastro.lift()
    janela_cadastro.focus_force()
    janela_cadastro.grab_set()

    ctk.CTkLabel(janela_cadastro, text="Título").pack(pady=5)
    entry_titulo = ctk.CTkEntry(janela_cadastro)
    entry_titulo.pack()

    ctk.CTkLabel(janela_cadastro, text="Autor").pack(pady=5)
    entry_autor = ctk.CTkEntry(janela_cadastro)
    entry_autor.pack()

    ctk.CTkLabel(janela_cadastro, text="Data de Publicação").pack(pady=5)
    entry_data = ctk.CTkEntry(janela_cadastro)
    entry_data.pack()

    ctk.CTkLabel(janela_cadastro, text="Gênero").pack(pady=5)
    entry_genero = ctk.CTkEntry(janela_cadastro)
    entry_genero.pack()

    ctk.CTkLabel(janela_cadastro, text="Quantidade de Livros").pack(pady=5)
    entry_qtd = ctk.CTkEntry(janela_cadastro)
    entry_qtd.pack()

    ctk.CTkButton(janela_cadastro, text="Salvar", command=salvar).pack(pady=15)
