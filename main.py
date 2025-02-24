import argparse
import multiprocessing
import time

import source as s
import destination as d


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Covert channel emulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--message', help='data to transfer via covert channel', required=False, dest='msg', type=str)
    parser.add_argument('-dp', '--destination_port', help='Listening port at client-side', required=False, dest='dport', type=int, default=1337)
    return parser.parse_args()

def main():
    args = parse_args()
    dport = args.dport

    client_process = multiprocessing.Process(target=d.init_client, args=(dport,))
    server_process = multiprocessing.Process(target=s.init_server, args=(dport,))
    client_process.daemon = True
    server_process.daemon = True

    client_process.start()
    server_process.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client_process.terminate()
        server_process.terminate()
        client_process.join()
        server_process.join()


if __name__ == "__main__":
    main()