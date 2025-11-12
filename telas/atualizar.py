import customtkinter as ctk
from tkinter import messagebox

def atualizar_livro(app, cur, conexao, centralizar):
    def buscar():
        codigo = entry_codigo.get()
        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código do livro!")
            return

        cur.execute("SELECT * FROM livro WHERE codigo=?", (codigo,))
        livro = cur.fetchone()

        if not livro:
            messagebox.showwarning("Aviso", "Livro não encontrado!")
            return

        entry_titulo.delete(0, 'end')
        entry_autor.delete(0, 'end')
        entry_data.delete(0, 'end')
        entry_genero.delete(0, 'end')
        entry_qtd.delete(0, 'end')

        entry_titulo.insert(0, livro[1])
        entry_autor.insert(0, livro[2])
        entry_data.insert(0, livro[3])
        entry_genero.insert(0, livro[4])
        entry_qtd.insert(0, livro[5])

    def salvar():
        codigo = entry_codigo.get()
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        data_publicacao = entry_data.get()
        genero = entry_genero.get()
        qtd_livros = entry_qtd.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código!")
            return

        cur.execute(
            "UPDATE livro SET titulo=?, autor=?, data_publicacao=?, genero=?, qtd_livros=? WHERE codigo=?",
            (titulo, autor, data_publicacao, genero, int(qtd_livros), int(codigo))
        )
        conexao.commit()
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
        janela_atualizacao.destroy()

    janela_atualizacao = ctk.CTkToplevel(app)
    janela_atualizacao.title("Atualizar Livro")
    centralizar(janela_atualizacao, 350, 550)
    janela_atualizacao.lift()
    janela_atualizacao.focus_force()
    janela_atualizacao.grab_set()

    ctk.CTkLabel(janela_atualizacao, text="Código do Livro").pack(pady=5)
    entry_codigo = ctk.CTkEntry(janela_atualizacao)
    entry_codigo.pack()

    ctk.CTkButton(janela_atualizacao, text="Buscar", command=buscar).pack(pady=5)

    ctk.CTkLabel(janela_atualizacao, text="Título").pack(pady=5)
    entry_titulo = ctk.CTkEntry(janela_atualizacao)
    entry_titulo.pack()

    ctk.CTkLabel(janela_atualizacao, text="Autor").pack(pady=5)
    entry_autor = ctk.CTkEntry(janela_atualizacao)
    entry_autor.pack()

    ctk.CTkLabel(janela_atualizacao, text="Data de Publicação").pack(pady=5)
    entry_data = ctk.CTkEntry(janela_atualizacao)
    entry_data.pack()

    ctk.CTkLabel(janela_atualizacao, text="Gênero").pack(pady=5)
    entry_genero = ctk.CTkEntry(janela_atualizacao)
    entry_genero.pack()

    ctk.CTkLabel(janela_atualizacao, text="Quantidade").pack(pady=5)
    entry_qtd = ctk.CTkEntry(janela_atualizacao)
    entry_qtd.pack()

    ctk.CTkButton(janela_atualizacao, text="Salvar Alterações", command=salvar).pack(pady=15)
