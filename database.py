import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "studio.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            template_type TEXT NOT NULL,
            tone TEXT NOT NULL,
            length TEXT NOT NULL,
            audience TEXT NOT NULL,
            prompt_used TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_all_articles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles ORDER BY created_at DESC")
    rows = cursor.fetchall()
    articles = [dict(row) for row in rows]
    conn.close()
    return articles

def get_article(article_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
    row = cursor.fetchone()
    article = dict(row) if row else None
    conn.close()
    return article

def create_article(title: str, content: str, template_type: str, tone: str, length: str, audience: str, prompt_used: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO articles (title, content, template_type, tone, length, audience, prompt_used)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, content, template_type, tone, length, audience, prompt_used))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return get_article(new_id)

def update_article(article_id: int, title: str, content: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE articles
        SET title = ?, content = ?
        WHERE id = ?
    """, (title, content, article_id))
    conn.commit()
    conn.close()
    return get_article(article_id)

def delete_article(article_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()
    return True
