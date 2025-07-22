# tcp_multithread_server.py
import socket
import threading
import time


def handle_client(conn, addr, count):
    print(f"[+] İstemci {addr} için iş parçacığı başlatıldı.")

    start_time = time.time()
    data = conn.recv(1024).decode()
    print(f"[{addr}] Gelen veri: {data}")

    filename = f"alınan_dosya_{count}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)

    time.sleep(10)
    conn.send("Dosya başarıyla alındı.".encode())
    conn.close()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"[*] {addr} bağlantısı kapatıldı. İşlem süresi: {elapsed_time:.4f} saniye.\n")
    print(f"[*] {addr} bağlantısı kapatıldı.\n")


def start_server():
    host = '127.0.0.1'
    port = 5006
    connection_count = 0

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[+] Multithreaded Sunucu başlatıldı: {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        connection_count += 1
        thread = threading.Thread(target=handle_client, args=(conn, addr, connection_count))
        thread.start()
        print(f"[#] Aktif thread sayısı: {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
