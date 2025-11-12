import customtkinter as ctk
from tkinter import messagebox

def excluir_livro(app, cur, conexao, centralizar):
    def deletar():
        codigo = entry_codigo.get().strip()

        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código!")
            return

        # Verifica se o código existe no banco
        cur.execute("SELECT * FROM livro WHERE codigo=?", (codigo,))
        livro = cur.fetchone()

        if not livro:
            messagebox.showerror("Erro", "Código inválido! Nenhum livro encontrado.")
            return

        # Se existir, exclui
        cur.execute("DELETE FROM livro WHERE codigo=?", (codigo,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
        janela_exclusao.destroy()

    janela_exclusao = ctk.CTkToplevel(app)
    janela_exclusao.title("Excluir Livro")
    centralizar(janela_exclusao, 300, 200)
    janela_exclusao.lift()
    janela_exclusao.focus_force()
    janela_exclusao.grab_set()

    ctk.CTkLabel(janela_exclusao, text="Código do Livro").pack(pady=10)
    entry_codigo = ctk.CTkEntry(janela_exclusao)
    entry_codigo.pack()

    ctk.CTkButton(janela_exclusao, text="Excluir", command=deletar).pack(pady=20)
