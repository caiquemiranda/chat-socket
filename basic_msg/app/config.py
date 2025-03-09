"""
Configuration module for the Message Terminal
"""
import os
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment variables"""
    load_dotenv()
    
    return {
        'server': {
            'host': os.getenv('HOST', 'localhost'),
            'port': int(os.getenv('PORT', 5001))
        },
        'database': {
            'file': os.getenv('DB_FILE', 'messages.db')
        },
        'app': {
            'title': os.getenv('APP_TITLE', 'Message Terminal'),
            'icon': os.getenv('APP_ICON', '🖥️'),
            'theme': os.getenv('APP_THEME', 'dark')
        },
        'style': {
            'primary_color': os.getenv('PRIMARY_COLOR', '#00ff00'),
            'bg_color': os.getenv('BG_COLOR', '#0a0a0a'),
            'secondary_bg': os.getenv('SECONDARY_BG', '#111111')
        }
    } 