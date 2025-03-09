"""
Database management module for the Message Terminal
"""
import sqlite3
from datetime import datetime
import os

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.init_db()
    
    def init_db(self):
        """Initialize the database"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS mensagens
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    message TEXT,
                    local INTEGER)''')
        conn.commit()
        conn.close()
    
    def add_message(self, msg, is_local=True):
        """Add message to database"""
        try:
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO mensagens (timestamp, message, local) VALUES (?, ?, ?)",
                    (timestamp, msg, 1 if is_local else 0))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error adding message: {e}")
            return False
    
    def load_messages(self):
        """Load messages from database"""
        try:
            if not os.path.exists(self.db_file):
                return []
            
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()
            c.execute("SELECT timestamp, message, local FROM mensagens ORDER BY id ASC")
            messages = []
            for ts, msg, local in c.fetchall():
                try:
                    data = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    try:
                        data = datetime.strptime(ts, "%d/%m/%Y, %H:%M:%S")
                    except ValueError:
                        data = datetime.now()
                
                ts_formatted = data.strftime("%d/%m/%Y %H:%M:%S")
                prefix = "<<" if local else ">>"
                messages.append(f"[{ts_formatted}] {prefix} {msg}")
            conn.close()
            return messages
            
        except Exception as e:
            print(f"Error loading messages: {e}")
            return []
    
    def clear_messages(self):
        """Clear all messages"""
        try:
            if os.path.exists(self.db_file):
                os.remove(self.db_file)
            self.init_db()
            return True
        except Exception as e:
            print(f"Error clearing messages: {e}")
            return False 