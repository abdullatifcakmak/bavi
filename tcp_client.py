# tcp_client.py
import socket

def start_client():
    host = '127.0.0.1'
    port = 5006

    with open("gonderilecek_dosya.txt", "r", encoding="utf-8") as f:
        file_content = f.read()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(file_content.encode())

    response = client_socket.recv(1024).decode()
    print(f"[Sunucu]: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
