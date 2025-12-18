print("CLIENT 2 SCRIPT STARTED")
import socket

from numpy import rint
from error_detection.parity import generate_parity
from error_detection.crc16 import generate_crc16
from error_detection.hamming import generate_hamming
from error_detection.checksum import generate_checksum

HOST = "localhost"
PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Client 2 listening...")

        conn, _ = s.accept()
        with conn:
            packet = conn.recv(1024).decode()
            data, method, incoming = packet.split("|")

            if method == "PARITY":
                computed = generate_parity(data)
            elif method == "CRC16":
                computed = generate_crc16(data)
            elif method == "HAMMING":
                from error_detection.hamming import check_and_correct_hamming

                corrected_data, corrected, positions = check_and_correct_hamming(incoming)

                print("Received (raw) Data:", data, flush=True)
                print("Decoded Data from Hamming:", corrected_data, flush=True)

                if corrected:
                    print("Error detected at bit positions:", positions, flush=True)
                    print("Status: SINGLE-BIT ERROR CORRECTED", flush=True)
                else:
                    if corrected_data != data:
                        print("Status: DATA CORRUPTED (Unprotected field modified)", flush=True)
                    else:
                        print("Status: DATA CORRECT", flush=True)

                exit()
            elif method == "CHECKSUM":
                computed = generate_checksum(data)

            print("Received Data:", data)
            print("Method:", method)
            print("Sent Check Bits:", incoming)
            print("Computed Check Bits:", computed)
            print("Status:", "DATA CORRECT" if incoming == computed else "DATA CORRUPTED")

if __name__ == "__main__":
    main()
