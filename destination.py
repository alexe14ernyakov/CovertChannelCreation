import socket
import time

HOST = '0.0.0.0'
BUFFER_SIZE = 1500
BASE_CHARACTER = str(chr(int('11111111', 2)))


def init_client(port: int, interval: int, covchan: bool):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, port))
        print(f"CLIENT   |   Listen for messages on port {port}")

        if covchan:
            secret: str = ''
            t1: float = time.time()

            while True:
                receive_packet(sock)
                t2: float = time.time()
                delay = t2 - t1
                t1 = t2

                bit = "0" if delay < interval else "1"
                secret += bit

                if len(secret) % 8 == 0:
                    decoded_secret: str = bin_to_str(secret)
                    if decoded_secret and decoded_secret[-1] != BASE_CHARACTER:
                        print(f"CLIENT   |   New character of secret received       : '{decoded_secret}'")
                    else:
                        print(f"CLIENT   |   Secret fully received: '{decoded_secret.split(BASE_CHARACTER)[0]}'")    
        else:
            while True:
                receive_packet(sock)


def receive_packet(socket: socket.socket):
    data, addr = socket.recvfrom(BUFFER_SIZE)
    print(f"CLIENT   |   Received message from {addr[0]:>10}:{addr[1]:<5} : '{data.decode()}'")


def bin_to_str(bin_str: str) -> str:
    try:
        result = "".join(chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8))
        return result
    except Exception as e:
        print(f"CLIENT   |   ERROR : {e}")
    return None
    