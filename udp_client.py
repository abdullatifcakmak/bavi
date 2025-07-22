# udp_client.py
import socket

def start_client():
    host = '127.0.0.1'
    port = 6001

    with open("gonderilecek_dosya.txt", "r", encoding="utf-8") as f:
        content = f.read()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(content.encode(), (host, port))

    print("[✓] Dosya gönderildi.")
    client_socket.close()

if __name__ == "__main__":
    start_client()
