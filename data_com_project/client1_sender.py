import socket
from error_detection.parity import generate_parity
from error_detection.crc16 import generate_crc16
from error_detection.hamming import generate_hamming
from error_detection.checksum import generate_checksum

HOST = "localhost"
PORT = 5000

print("CLIENT 1 STARTED", flush=True)

data = input("Enter text to send: ")

print("\nSelect Error Detection Method:", flush=True)
print("1. Parity", flush=True)
print("2. CRC16", flush=True)
print("3. Hamming Code", flush=True)
print("4. Internet Checksum", flush=True)

choice = input("Choice: ").strip()

if choice == "1":
    method = "PARITY"
    control = generate_parity(data)
elif choice == "2":
    method = "CRC16"
    control = generate_crc16(data)
elif choice == "3":
    method = "HAMMING"
    control = generate_hamming(data)
elif choice == "4":
    method = "CHECKSUM"
    control = generate_checksum(data)
else:
    print("Invalid choice", flush=True)
    exit()

packet = f"{data}|{method}|{control}"

print("Connecting to server...", flush=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet.encode())

print("Packet sent:", packet, flush=True)
