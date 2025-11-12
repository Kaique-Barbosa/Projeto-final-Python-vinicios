import customtkinter as ctk

def listar_livros(app, cur, centralizar):
    janela_listagem = ctk.CTkToplevel(app)
    janela_listagem.title("Lista de Livros")
    centralizar(janela_listagem, 650, 450)
    janela_listagem.lift()
    janela_listagem.focus_force()
    janela_listagem.grab_set()

    frame_lista = ctk.CTkScrollableFrame(janela_listagem, width=600, height=350)
    frame_lista.pack(pady=10)

    cur.execute("SELECT * FROM livro")
    livros = cur.fetchall()

    if not livros:
        ctk.CTkLabel(frame_lista, text="Nenhum livro cadastrado.").pack(pady=10)
        return

    for l in livros:
        texto = f"Código: {l[0]} | {l[1]} | Autor: {l[2]} | Publicação: {l[3]} | Gênero: {l[4]} | Qtd: {l[5]}"
        ctk.CTkLabel(frame_lista, text=texto, anchor="w", justify="left").pack(anchor="w", padx=10)
