"""
Styles module for the Message Terminal
"""

def get_css_styles(primary_color, bg_color, secondary_bg):
    """Get CSS styles for the application"""
    return f"""
    <style>
    /* Reset e Base */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    
    /* Esconder elementos Streamlit */
    #MainMenu {{visibility: hidden !important;}}
    header {{visibility: hidden !important;}}
    footer {{visibility: hidden !important;}}
    
    /* Estilo base do app */
    .stApp {{
        background-color: {bg_color} !important;
        color: {primary_color} !important;
    }}
    
    /* Título */
    .title-text {{
        color: {primary_color} !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 10px {primary_color} !important;
        padding: 10px !important;
        background-color: {secondary_bg} !important;
        border: 1px solid {primary_color} !important;
        border-radius: 5px !important;
        margin-bottom: 10px !important;
    }}
    
    /* Texto do terminal */
    .terminal-text {{
        font-family: 'Courier New', monospace !important;
        color: {primary_color} !important;
        background-color: {bg_color} !important;
        padding: 5px 10px !important;
        border-left: 2px solid {primary_color} !important;
        margin: 2px 0 !important;
    }}
    
    /* Status */
    .status-text {{
        color: {primary_color} !important;
        font-family: 'Courier New', monospace !important;
        font-size: 0.8em !important;
        padding: 5px !important;
        margin-bottom: 10px !important;
        border-bottom: 1px solid {primary_color} !important;
    }}
    
    /* Botões */
    .stButton > button {{
        width: 100% !important;
        background-color: {bg_color} !important;
        color: {primary_color} !important;
        border: 1px solid {primary_color} !important;
        font-family: 'Courier New', monospace !important;
        transition: all 0.3s ease !important;
    }}
    
    .stButton > button:hover {{
        background-color: {primary_color} !important;
        color: {bg_color} !important;
    }}
    
    /* Input de texto */
    .stTextInput > div > div > input {{
        background-color: {secondary_bg} !important;
        color: {primary_color} !important;
        border: 1px solid {primary_color} !important;
        font-family: 'Courier New', monospace !important;
    }}
    
    /* Container de mensagens */
    .messages-container {{
        height: 65vh !important;
        overflow-y: auto !important;
        padding: 10px !important;
        background-color: {bg_color} !important;
        border: 1px solid {primary_color} !important;
        margin: 10px 0 !important;
    }}

    /* Alertas */
    .stAlert {{
        background-color: {secondary_bg} !important;
        color: {primary_color} !important;
        border: 1px solid {primary_color} !important;
    }}

    /* Containers vazios */
    .element-container:empty {{
        display: none !important;
    }}

    .stMarkdown:empty {{
        display: none !important;
    }}

    /* Scrollbar personalizada */
    ::-webkit-scrollbar {{
        width: 10px;
    }}

    ::-webkit-scrollbar-track {{
        background: {bg_color};
    }}

    ::-webkit-scrollbar-thumb {{
        background: {primary_color};
        border-radius: 5px;
    }}

    /* Variáveis CSS */
    :root {{
        --primary-color: {primary_color};
        --bg-color: {bg_color};
        --secondary-bg: {secondary_bg};
    }}
    </style>
    """ 