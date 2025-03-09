"""
Message handling module for the Message Terminal
"""
import socket
import time
import threading
import streamlit as st

class MessageHandler:
    def __init__(self, host, port, db_manager):
        self.host = host
        self.port = port
        self.db_manager = db_manager
        self.running = True
    
    def start_receiver(self):
        """Start the message receiver thread"""
        if 'receiver_thread' not in st.session_state:
            receiver_thread = threading.Thread(target=self._receive_messages, daemon=True)
            receiver_thread.start()
            st.session_state['receiver_thread'] = receiver_thread
    
    def _receive_messages(self):
        """Thread to receive messages"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            sock.bind((self.host, self.port))
            sock.listen(1)
            print(f"Server listening on {self.host}:{self.port}")
            
            while self.running:
                try:
                    conn, addr = sock.accept()
                    with conn:
                        data = conn.recv(1024)
                        if data:
                            msg = data.decode('utf-8')
                            if msg.strip():
                                print(f"Received message: {msg}")
                                self.db_manager.add_message(msg, False)
                except Exception as e:
                    print(f"Connection error: {e}")
                    time.sleep(0.1)
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            sock.close()
    
    def stop_receiver(self):
        """Stop the message receiver"""
        self.running = False 