import socket


HOST = '0.0.0.0'
BUFFER_SIZE = 1500


def init_client(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, port))
        print(f"Server initialized on port {port}")

        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"CLIENT   |   Received message from {addr[0]}:{addr[1]} : {data.decode()}")