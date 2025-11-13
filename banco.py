# -------------------- CLASSE DE GERENCIAMENTO DO BANCO DE DADOS --------------------
# Este arquivo aplica o conceito de Programação Orientada a Objetos (POO)
# encapsulando todas as operações SQL dentro da classe Banco.
# Além disso, faz uso de DICIONÁRIOS nas funções de inserção e atualização.

import sqlite3 as db_sqlite3

class Banco:
    def __init__(self, nome_banco="biblioteca.db"):
        # Construtor da classe Banco - cria a conexão e garante que a tabela exista
        self.conexao = db_sqlite3.connect(nome_banco)
        self.cur = self.conexao.cursor()
        self.criar_tabela()

    # -------------------- CRIAÇÃO DA TABELA --------------------
    def criar_tabela(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS livro (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            data_publicacao TEXT NOT NULL,
            genero TEXT NOT NULL,
            qtd_livros INTEGER NOT NULL
        )
        """)
        self.conexao.commit()

    # -------------------- INSERIR NOVO LIVRO --------------------
    def inserir(self, dados: dict):
        """
        Recebe um dicionário com as chaves:
        'titulo', 'autor', 'data_publicacao', 'genero', 'qtd_livros'
        e insere os valores no banco de dados.
        """
        self.cur.execute("""
            INSERT INTO livro (titulo, autor, data_publicacao, genero, qtd_livros)
            VALUES (:titulo, :autor, :data_publicacao, :genero, :qtd_livros)
        """, dados)
        self.conexao.commit()

    # -------------------- LISTAR TODOS OS LIVROS --------------------
    def listar(self):
        self.cur.execute("SELECT * FROM livro")
        return self.cur.fetchall()

    # -------------------- BUSCAR LIVRO PELO CÓDIGO --------------------
    def buscar(self, codigo):
        self.cur.execute("SELECT * FROM livro WHERE codigo=?", (codigo,))
        return self.cur.fetchone()

    # -------------------- ATUALIZAR LIVRO EXISTENTE --------------------
    def atualizar(self, codigo, dados: dict):
        """
        Atualiza os campos do livro de acordo com o código fornecido.
        Usa dicionário (dados) para atualizar os valores.
        """
        self.cur.execute("""
            UPDATE livro
            SET titulo=:titulo, autor=:autor, data_publicacao=:data_publicacao,
                genero=:genero, qtd_livros=:qtd_livros
            WHERE codigo=:codigo
        """, {**dados, "codigo": codigo})
        self.conexao.commit()

    # -------------------- EXCLUIR LIVRO --------------------
    def excluir(self, codigo):
        self.cur.execute("DELETE FROM livro WHERE codigo=?", (codigo,))
        self.conexao.commit()

    # -------------------- FECHAR CONEXÃO --------------------
    def fechar(self):
        self.conexao.close()
