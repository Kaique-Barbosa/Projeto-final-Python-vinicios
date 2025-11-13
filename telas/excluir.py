import customtkinter as ctk 
from tkinter import messagebox 

# Função responsável por excluir um livro do banco de dados
# Parâmetros:
# app → janela principal
# banco → instância da classe Banco (POO)
# centralizar → função auxiliar que posiciona a janela no centro da tela
def excluir_livro(app, banco, centralizar):
    
    # ------------------- FUNÇÃO INTERNA: DELETAR LIVRO -------------------
    def deletar():
        codigo = entry_codigo.get().strip() 

        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código!") 
            return 

        # Busca pelo livro usando método da classe Banco
        livro = banco.buscar(codigo)
        if not livro:
            messagebox.showerror("Erro", "Código inválido! Nenhum livro encontrado.")
            return

        # Se o livro existir, exclui pelo método da classe Banco (POO)
        banco.excluir(codigo)
        messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
        janela_exclusao.destroy()

    # ------------------- CONFIGURAÇÃO DA JANELA -------------------
    janela_exclusao = ctk.CTkToplevel(app)  
    janela_exclusao.title("Excluir Livro") 
    centralizar(janela_exclusao, 300, 200) 
    janela_exclusao.lift() 
    janela_exclusao.focus_force() 
    janela_exclusao.grab_set() 

    # ------------------- CAMPOS E BOTÃO -------------------
    ctk.CTkLabel(janela_exclusao, text="Código do Livro").pack(pady=10) 
    entry_codigo = ctk.CTkEntry(janela_exclusao)
    entry_codigo.pack() 

    ctk.CTkButton(janela_exclusao, text="Excluir", command=deletar).pack(pady=20) 
