import customtkinter as ctk # Importa a biblioteca CustomTkinter

# Função responsável por exibir todos os livros cadastrados no banco de dados
# Parâmetros:
# app → janela principal da aplicação
# banco → instância da classe Banco (POO)
# centralizar → função auxiliar para posicionar a janela no centro da tela
def listar_livros(app, banco, centralizar):
    
    # ------------------- CONFIGURAÇÃO DA JANELA -------------------
    janela_listagem = ctk.CTkToplevel(app) 
    janela_listagem.title("Lista de Livros") 
    centralizar(janela_listagem, 650, 450) 
    janela_listagem.lift() 
    janela_listagem.focus_force() 
    janela_listagem.grab_set() 

    # ------------------- ÁREA DE LISTAGEM (ROLÁVEL) -------------------
    frame_lista = ctk.CTkScrollableFrame(janela_listagem, width=600, height=350)
    frame_lista.pack(pady=10) 

    # ------------------- CONSULTA AO BANCO DE DADOS (POO) ------------------
    livros = banco.listar()  # Chama o método listar() da classe Banco

    # ------------------- VERIFICA SE EXISTEM LIVROS -------------------
    if not livros: 
        ctk.CTkLabel(frame_lista, text="Nenhum livro cadastrado.").pack(pady=10)
        return 

    # ------------------- EXIBE OS LIVROS NA TELA -------------------
    for l in livros: 
        texto = f"Código: {l[0]} | {l[1]} | Autor: {l[2]} | Publicação: {l[3]} | Gênero: {l[4]} | Qtd: {l[5]}"
        ctk.CTkLabel(frame_lista, text=texto, anchor="w", justify="left").pack(anchor="w", padx=10, pady=5)
