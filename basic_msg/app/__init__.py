"""
Message Terminal Application
"""
from .config import load_config
from .database import DatabaseManager
from .interface import Interface
from .messaging import MessageHandler
from .styles import get_css_styles

__version__ = "1.0.0" 