import socket
import multiprocessing
import time
import random
import string


DESTINATION_IP = '127.0.0.1'
SENDING_INTERVAL = 2
MIN_PACKET_SIZE = 5
MAX_PACKET_SIZE = 100


def init_server(port: int, msg: str | None):
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (DESTINATION_IP, port)
    print(f"SERVER   |   Initialized packet sending to {DESTINATION_IP}:{port}")

    msg_queue = multiprocessing.Queue()

    generator_process = multiprocessing.Process(target=message_generator, args=(msg_queue,))
    sender_process = multiprocessing.Process(target=message_sender, args=(sock, address, msg_queue, msg))

    generator_process.start()
    sender_process.start()

    generator_process.join()
    sender_process.join()
                

def message_generator(queue: multiprocessing.Queue):
    while True:
        message = random_message()
        queue.put(message)
        time.sleep(SENDING_INTERVAL)


def message_sender(socket: socket.socket, addr: tuple, buffer: multiprocessing.Queue, secret: str):
    while True:
        if bool(secret):
            bin_msg = bin_string(secret)

            for bit in bin_msg:
                if bit == '0':
                    time.sleep(SENDING_INTERVAL * 0.5)
                    
                    if not buffer.empty():
                        message = buffer.get()
                    else:
                        message = 'FICTITIOUS' + random_message()
                    send_packet(socket, message, addr)
                else:
                    time.sleep(SENDING_INTERVAL * 1.5)

                    if not buffer.empty():
                        message = buffer.get()
                    else:
                        message = 'FICTITIOUS' + random_message()
                    send_packet(socket, message, addr)
            secret = None
        else:
            time.sleep(SENDING_INTERVAL)
            if not buffer.empty():
                message = buffer.get()
                send_packet(socket, message, addr)


def send_packet(socket: socket.socket, text: str, addr: tuple):
    try:
        socket.sendto(text.encode(), addr)
        print(f"SERVER   |   Send message to       {addr[0]:>10}:{addr[1]:<5} : '{text}'")
    except Exception as e:
        print(f"SERVER   |   ERROR: {e}")


def random_message() -> str:
    lenght = random.randint(MIN_PACKET_SIZE, MAX_PACKET_SIZE)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=lenght))

def bin_string(string: str) -> str:
    return ''.join(format(byte, '08b') for byte in string.encode())
