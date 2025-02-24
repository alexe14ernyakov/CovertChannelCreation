import socket
import time
import random
import string


DESTINATION_IP = '127.0.0.1'
SENDING_INTERVAL = 2
MIN_PACKET_SIZE = 5
MAX_PACKET_SIZE = 1500


def init_server(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            message = random_message()
            try:
                sock.sendto(message.encode(), (DESTINATION_IP, port))
                print(f"SERVER   |   Send message '{message}' to {DESTINATION_IP}:{port}")
            except Exception as e:
                print(f"ERROR: {e}")

            time.sleep(SENDING_INTERVAL)


def random_message() -> str:
    lenght = random.randint(MIN_PACKET_SIZE, MAX_PACKET_SIZE)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=lenght))
