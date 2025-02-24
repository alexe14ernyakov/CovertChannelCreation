import socket
import time


DESTINATION_IP = '127.0.0.1'


def init_server(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        i = 0
        while True:
            message = f"Message {i}"
            try:
                sock.sendto(message.encode(), (DESTINATION_IP, port))
                print(f"SERVER   |   Send message '{message}' to {DESTINATION_IP}:{port}")
            except Exception as e:
                print(f"ERROR: {e}")

            i += 1
            time.sleep(2)
