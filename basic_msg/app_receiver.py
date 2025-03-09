"""
Message Terminal - Main Application
"""
import streamlit as st
from app import (
    load_config,
    DatabaseManager,
    Interface,
    MessageHandler,
    get_css_styles
)

def main():
    # Load configuration
    config = load_config()
    
    # Initialize components
    db_manager = DatabaseManager(config['database']['file'])
    interface = Interface(db_manager, config)
    
    # Setup page first
    interface.setup_page()
    
    # Apply base styles
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stApp {
            background-color: #0a0a0a !important;
        }
        
        div[data-testid="stToolbar"] {
            display: none;
        }
        
        div[data-testid="stDecoration"] {
            display: none;
        }
        
        div[data-testid="stStatusWidget"] {
            display: none;
        }
        
        section[data-testid="stSidebar"] {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Apply theme styles
    st.markdown(
        get_css_styles(
            config['style']['primary_color'],
            config['style']['bg_color'],
            config['style']['secondary_bg']
        ),
        unsafe_allow_html=True
    )
    
    # Initialize message handler
    message_handler = MessageHandler(
        config['server']['host'],
        config['server']['port'],
        db_manager
    )
    
    # Start message receiver
    message_handler.start_receiver()
    
    # Render interface components
    interface.render_header()
    messages_container = interface.render_messages()
    interface.render_input_area()
    interface.render_clear_button(messages_container)
    
    # Check for updates
    interface.check_updates()

if __name__ == "__main__":
    main() 