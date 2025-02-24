import socket


HOST = '0.0.0.0'
BUFFER_SIZE = 1500


def init_client(port: int, covchan: bool):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, port))
        print(f"CLIENT   |   Listen for messages on port {port}")

        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"CLIENT   |   Received message from {addr[0]:>10}:{addr[1]:<5} : '{data.decode()}'")