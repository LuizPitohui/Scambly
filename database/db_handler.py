import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "scambly.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            pontos INTEGER DEFAULT 0,
            sobrenome TEXT,
            endereco1 TEXT,
            endereco2 TEXT,
            cidade TEXT,
            estado TEXT,
            cep TEXT,
            pais TEXT
        );
    """)
    conn.commit()
    conn.close()


def inserir_usuario(nome, email, senha):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  # Email já existe

def verificar_credenciais(email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario  # None se não existir

def adicionar_pontos(email, pontos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET pontos = pontos + ? WHERE email = ?", (pontos, email))
    conn.commit()
    conn.close()
    
def buscar_dados_usuario(email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, pontos FROM usuarios WHERE email = ?", (email,))
    dados = cursor.fetchone()
    conn.close()
    return dados  # retorna (nome, pontos) ou None

def atualizar_dados_usuario(email_atual, novo_nome, novo_email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE usuarios SET nome = ?, email = ?
            WHERE email = ?
        """, (novo_nome, novo_email, email_atual))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao atualizar:", e)
        return False
    finally:
        conn.close()
