import customtkinter as ctk
from tkinter import messagebox

# Telas
from telas.cadastrar import cadastrar_livro
from telas.listar import listar_livros
from telas.atualizar import atualizar_livro
from telas.excluir import excluir_livro

# -------------------- IMPORTAÇÃO DA CLASSE POO --------------------
# A classe Banco está na raiz do projeto e controla toda a parte do banco de dados.
# Aqui aplicamos o conceito de POO instanciando a classe como um objeto.
from banco import Banco

# -------------------- CONFIGURAÇÕES  DE TEMAS DO CUSTOMCTK --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------- INSTÂNCIA DO BANCO DE DADOS (POO) --------------------
# Aqui criamos um objeto 'banco' da classe Banco, que gerencia todas as operações SQL.
banco = Banco()

# ------- FUNÇÃO PARA OBTER A LARGURA E ALTURA MONITOR E DEFINIR O TAMANHO DAS JANELAS --------------------
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# -------------------- JANELA PRINCIPAL --------------------
#  ESSA JANELA CONTÉM O MENU INICIAL DO SISTEMA
app = ctk.CTk()
app.title("Sistema da Biblioteca")
centralizar_janela(app, 400, 480)  # APP É A INSTÂNCIA DO CTK, 400 É A LARGURA E 480 A ALTURA

#  ABAIXO ESTÃO OS BOTOES CHAMANDO AS FUNÇÕES DAS TELAS
ctk.CTkLabel(app, text=" Gerenciamento de Livros", font=("Arial", 20)).pack(pady=15)

#  Cada botão chama sua respectiva função, passando:
#  app → janela principal, banco → instância da classe Banco, centralizar_janela → função auxiliar
ctk.CTkButton(app, text="Cadastrar Livro", command=lambda: cadastrar_livro(app, banco, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Listar Livros", command=lambda: listar_livros(app, banco, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Atualizar Livro", command=lambda: atualizar_livro(app, banco, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Excluir Livro", command=lambda: excluir_livro(app, banco, centralizar_janela)).pack(pady=8)
ctk.CTkButton(app, text="Sair", command=app.destroy).pack(pady=20)

# Inicia a aplicação
app.mainloop()

# Fecha a conexão do banco ao encerrar o programa
banco.fechar()
