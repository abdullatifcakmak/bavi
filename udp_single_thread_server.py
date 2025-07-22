# udp_single_thread_server.py
import socket
import time

def start_server():
    host = '127.0.0.1'
    port = 6000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"[+] UDP Sunucu başlatıldı: {host}:{port}")
    start_time = time.time()
    count = 0

    while True:
        data, addr = server_socket.recvfrom(4096)
        count += 1
        print(f"[{addr}] veri alındı. Dosya yazılıyor...")

        filename = f"udp_dosya_{count}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data.decode())
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[*] {addr} bağlantısı kapatıldı. İşlem süresi: {elapsed_time:.4f} saniye.\n")
        print(f"[✓] Dosya kaydedildi: {filename}\n")

if __name__ == "__main__":
    start_server()
