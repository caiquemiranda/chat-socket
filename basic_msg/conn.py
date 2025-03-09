import socket
import time
from datetime import datetime

# Configurações
HOST = 'localhost'
PORT = 5001  # Mesma porta do servidor

def enviar_mensagem(mensagem):
    try:
        # Criar novo socket para cada mensagem
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Tentar conectar
            s.connect((HOST, PORT))
            # Enviar mensagem
            s.sendall(mensagem.encode('utf-8'))
            print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Mensagem enviada: {mensagem}")
            return True
    except ConnectionRefusedError:
        print("❌ Erro: Servidor não está rodando. Certifique-se que o app_receiver.py está ativo.")
        return False
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem: {e}")
        return False

def main():
    print("="*50)
    print("📨 Sistema de Envio de Mensagens")
    print(f"🎯 Conectando ao servidor em {HOST}:{PORT}")
    print("💡 Digite 'sair' para encerrar o programa")
    print("="*50)
    
    # Tentar primeira conexão
    primeira_tentativa = True
    
    while True:
        try:
            if primeira_tentativa:
                # Verificar se o servidor está online
                if not enviar_mensagem("teste_conexao"):
                    input("Pressione ENTER para tentar novamente...")
                    continue
                primeira_tentativa = False
            
            mensagem = input("\n➤ Digite sua mensagem: ").strip()
            
            if not mensagem:
                continue
                
            if mensagem.lower() == 'sair':
                print("\n👋 Encerrando o programa...")
                break
            
            enviar_mensagem(mensagem)
            time.sleep(0.1)  # Pequeno delay entre mensagens
            
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
