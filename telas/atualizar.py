import customtkinter as ctk  
from tkinter import messagebox 

# Define a função principal para a tela de atualização
# 'app' é a janela principal, 'banco' é a instância da classe Banco (POO)
# 'centralizar' é a função de ajuda do main.py
def atualizar_livro(app, banco, centralizar):
    
    # --- FUNÇÃO INTERNA: BUSCAR ---
    # Esta função será executada quando o botão "Buscar" for clicado
    def buscar():
        codigo = entry_codigo.get()  # Pega o texto digitado no campo "entry_codigo"
        
        # Validação: Verifica se o campo de código não está vazio
        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código do livro!")
            return  

        # Executa a busca no banco de dados usando a classe Banco (POO)
        livro = banco.buscar(codigo)

        # Validação: Verifica se o livro foi encontrado
        if not livro:
            messagebox.showwarning("Aviso", "Livro não encontrado!")
            return  

        # --- Se o livro foi encontrado, preenche os campos ---
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

    # --- FUNÇÃO INTERNA: SALVAR ---
    # Esta função será executada quando o botão "Salvar Alterações" for clicado
    def salvar():
        codigo = entry_codigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Informe o código!")
            return

        # Criação de um dicionário com os dados atualizados ✅
        dados = {
            "titulo": entry_titulo.get(),
            "autor": entry_autor.get(),
            "data_publicacao": entry_data.get(),
            "genero": entry_genero.get(),
            "qtd_livros": int(entry_qtd.get())
        }

        # Chamada ao método POO da classe Banco
        banco.atualizar(codigo, dados)
        
        messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
        janela_atualizacao.destroy()

    # --- CONFIGURAÇÃO DA JANELA DE ATUALIZAÇÃO ---
    janela_atualizacao = ctk.CTkToplevel(app)
    janela_atualizacao.title("Atualizar Livro")  
    centralizar(janela_atualizacao, 350, 550)  
    janela_atualizacao.lift()
    janela_atualizacao.focus_force() 
    janela_atualizacao.grab_set()  

    # --- CRIAÇÃO DOS WIDGETS ---
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
