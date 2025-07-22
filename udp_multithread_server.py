# udp_multithread_server.py
import socket
import threading
import time


def handle_client(data, addr, count):
    print(f"[+] Thread başlatıldı: {addr}")
    start_time = time.time()
    filename = f"udp_mt_dosya_{count}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data.decode())
    time.sleep(10)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"[*] {addr} bağlantısı kapatıldı. İşlem süresi: {elapsed_time:.4f} saniye.\n")
    print(f"[✓] {filename} kaydedildi.\n")

def start_server():
    host = '127.0.0.1'
    port = 6001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"[+] UDP Multithread Sunucu: {host}:{port}")

    count = 0

    while True:
        data, addr = server_socket.recvfrom(4096)
        count += 1

        thread = threading.Thread(target=handle_client, args=(data, addr, count))
        thread.start()

        print(f"[*] Aktif thread sayısı: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
