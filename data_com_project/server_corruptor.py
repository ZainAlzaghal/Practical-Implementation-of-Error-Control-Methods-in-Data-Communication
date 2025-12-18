import socket
from error_injection.injector import corrupt_data

print("\nSelect Error Injection Method:", flush=True)
print("1. Bit Flip", flush=True)
print("2. Character Substitution", flush=True)
print("3. Character Deletion", flush=True)
print("4. Random Character Insertion", flush=True)
print("5. Character Swapping", flush=True)
print("6. Burst Error", flush=True)

error_choice = input("Choice: ").strip()


HOST = "localhost"
PORT = 5000
CLIENT2_PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server listening...")

        conn, _ = s.accept()
        with conn:
            packet = conn.recv(1024).decode()
            data, method, control = packet.split("|")

            corrupted = corrupt_data(data, error_choice)
            new_packet = f"{corrupted}|{method}|{control}"

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                s2.connect((HOST, CLIENT2_PORT))
                s2.sendall(new_packet.encode())

if __name__ == "__main__":
    main()
