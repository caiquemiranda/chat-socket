import streamlit as st
import time
from datetime import datetime
import sqlite3
import json

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Chat em Tempo Real",
    page_icon="💬",
    layout="wide"
)

# Configuração do banco de dados
def init_db():
    conn = sqlite3.connect('chat.db', check_same_thread=False)
    c = conn.cursor()
    
    # Criar tabela de usuários se não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS users
        (user_id TEXT PRIMARY KEY)
    ''')
    
    # Criar tabela de mensagens se não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages
        (user TEXT, text TEXT, timestamp TEXT)
    ''')
    
    conn.commit()
    return conn

# Inicializar o banco de dados
conn = init_db()

# Funções de banco de dados
def add_user(user_id):
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def remove_user(user_id):
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()

def get_users():
    c = conn.cursor()
    c.execute('SELECT user_id FROM users')
    return {row[0] for row in c.fetchall()}

def add_message(user, text, timestamp):
    c = conn.cursor()
    c.execute('INSERT INTO messages (user, text, timestamp) VALUES (?, ?, ?)',
              (user, text, timestamp))
    conn.commit()

def get_messages():
    c = conn.cursor()
    c.execute('SELECT user, text, timestamp FROM messages')
    return [{"user": row[0], "text": row[1], "timestamp": row[2]} 
            for row in c.fetchall()]

# Inicialização das variáveis de estado
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# Interface de login
if st.session_state.current_user is None:
    st.title("Bem-vindo ao Chat em Tempo Real! 💬")
    st.subheader("Chat Compartilhado - Todos conversam juntos!")
    
    with st.form("login_form"):
        user_id = st.text_input("Digite seu ID para entrar no chat:")
        submit_button = st.form_submit_button("Entrar")
        
        if submit_button:
            if user_id.strip() == "":
                st.error("Por favor, digite um ID válido!")
            elif user_id in get_users():
                st.error("Este ID já está em uso. Por favor, escolha outro!")
            else:
                st.session_state.current_user = user_id
                add_user(user_id)
                st.rerun()

# Interface do chat
else:
    # Layout em duas colunas
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title(f"Chat em Tempo Real 💬")
    
    with col2:
        st.sidebar.title("Usuários Online")
        st.sidebar.write("👥 Participantes:")
        for user in sorted(get_users()):
            if user == st.session_state.current_user:
                st.sidebar.write(f"👤 **Você** ({user})")
            else:
                st.sidebar.write(f"👤 {user}")
                
        if st.sidebar.button("Sair do Chat"):
            remove_user(st.session_state.current_user)
            st.session_state.current_user = None
            st.rerun()
    
    # Área de mensagens com estilo
    chat_container = st.container()
    
    # Formulário para enviar mensagens
    with st.form("message_form", clear_on_submit=True):
        message = st.text_input("Digite sua mensagem:", key="message_input")
        col1, col2 = st.columns([6, 1])
        with col2:
            send_button = st.form_submit_button("Enviar 📤")
        
        if send_button and message.strip():
            timestamp = datetime.now().strftime("%H:%M:%S")
            add_message(st.session_state.current_user, message, timestamp)
    
    # Exibição das mensagens com estilo
    with chat_container:
        st.write("---")
        for msg in get_messages():
            if msg["user"] == st.session_state.current_user:
                st.write(f'🗨️ **Você** ({msg["timestamp"]}): {msg["text"]}')
            else:
                st.write(f'💬 **{msg["user"]}** ({msg["timestamp"]}): {msg["text"]}')
        st.write("---")
    
    # Auto-atualização da página
    time.sleep(1)
    st.rerun() 