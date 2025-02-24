import argparse
import multiprocessing
import time

import source as s
import destination as d


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Covert channel emulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--message', help='Data to transfer via covert channel', required=False, dest='msg', type=str)
    parser.add_argument('-dp', '--destination_port', help='Listening port at client-side', required=False, dest='dport', type=int, default=1337)
    parser.add_argument('-i', '--interval', help='Interval between packet sending in network in regular mode', required=False, dest='interval', type=float, default=1)
    return parser.parse_args()

def main():
    args = parse_args()

    secret_message = args.msg
    dport = args.dport
    interval = args.interval

    client_process = multiprocessing.Process(target=d.init_client, args=(dport, interval, True if secret_message else False))
    server_process = multiprocessing.Process(target=s.init_server, args=(dport, interval, secret_message))

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