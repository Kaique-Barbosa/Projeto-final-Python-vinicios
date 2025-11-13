import customtkinter as ctk 
from tkinter import messagebox 

# Função responsável por abrir a janela e cadastrar um novo livro no banco de dados
# Parâmetros:
# app → janela principal da aplicação
# banco → instância da classe Banco (POO) que gerencia as operações SQL
# centralizar → função que posiciona a janela no centro da tela
def cadastrar_livro(app, banco, centralizar):
    
    # ------------------- FUNÇÃO INTERNA: SALVAR LIVRO -------------------
    def salvar():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        data_publicacao = entry_data.get()
        genero = entry_genero.get()
        qtd_livros = entry_qtd.get()

        # Verifica se algum campo está vazio
        if not titulo or not autor or not data_publicacao or not genero or not qtd_livros:
            messagebox.showwarning("Aviso", "Preencha todos os campos!") # Exibe aviso
            return # Interrompe a execução da função

        # ------------------- USO DE DICIONÁRIO -------------------
        # Aqui aplicamos o conceito de dicionário: os dados são armazenados em pares chave:valor
        dados = {
            "titulo": titulo,
            "autor": autor,
            "data_publicacao": data_publicacao,
            "genero": genero,
            "qtd_livros": int(qtd_livros)
        }

        # A classe Banco, em POO, é usada para inserir o registro no banco
        banco.inserir(dados)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")  # Exibe mensagem de sucesso
        janela_cadastro.destroy() # Fecha a janela após o cadastro

    # ------------------- CONFIGURAÇÃO DA JANELA -------------------
    janela_cadastro = ctk.CTkToplevel(app) # Cria uma nova janela "filha" da principal
    janela_cadastro.title("Cadastrar Livro") # Define o título da janela
    centralizar(janela_cadastro, 320, 400) # Centraliza a janela na tela com largura 320 e altura 400
    janela_cadastro.lift() # Garante que a janela fique na frente das outras
    janela_cadastro.focus_force() # Dá foco automático na nova janela
    janela_cadastro.grab_set() # Impede interação com outras janelas até que essa seja fechada

    # ------------------- CAMPOS DE ENTRADA -------------------
    # Campo: Título
    ctk.CTkLabel(janela_cadastro, text="Título").pack(pady=5) # Cria o rótulo
    entry_titulo = ctk.CTkEntry(janela_cadastro) # Campo de texto
    entry_titulo.pack() # Exibe o campo na tela

    # Campo: Autor
    ctk.CTkLabel(janela_cadastro, text="Autor").pack(pady=5)
    entry_autor = ctk.CTkEntry(janela_cadastro)
    entry_autor.pack()

    # Campo: Data de Publicação
    ctk.CTkLabel(janela_cadastro, text="Data de Publicação").pack(pady=5)
    entry_data = ctk.CTkEntry(janela_cadastro)
    entry_data.pack()

    # Campo: Gênero
    ctk.CTkLabel(janela_cadastro, text="Gênero").pack(pady=5)
    entry_genero = ctk.CTkEntry(janela_cadastro)
    entry_genero.pack()

    # Campo: Quantidade de Livros
    ctk.CTkLabel(janela_cadastro, text="Quantidade de Livros").pack(pady=5)
    entry_qtd = ctk.CTkEntry(janela_cadastro)
    entry_qtd.pack()

    # ------------------- BOTÃO DE SALVAR -------------------
    # Cria o botão que chama a função "salvar" ao ser clicado
    ctk.CTkButton(janela_cadastro, text="Salvar", command=salvar).pack(pady=15)
