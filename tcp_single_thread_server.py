# tcp_single_thread_server.py
import socket
import time


def start_server():
    host = '127.0.0.1'
    port = 5005

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[+] Sunucu {host}:{port} adresinde başlatıldı (Tek Thread)")

    while True:
        print("[*] İstemci bekleniyor...")
        conn, addr = server_socket.accept()
        print(f"[+] Bağlantı: {addr}")
        start_time = time.time()

        data = conn.recv(1024).decode()
        print(f"[>] Alınan veri: {data}")


        with open("alınan_dosya.txt", "w", encoding="utf-8") as f:
            f.write(data)
        time.sleep(10)
        conn.send("Dosya başarıyla alındı.".encode())
        conn.close()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[*] Bağlantı kapatıldı. İşlem süresi: {elapsed_time:.4f} saniye.\n")
        print("[*] Bağlantı kapatıldı.\n")

if __name__ == "__main__":
    start_server()
