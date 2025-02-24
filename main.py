import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Covert channel emulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--message', help='data to transfer via covert channel', required=False, dest='msg', type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    message = args.msg
    print(message)


if __name__ == "__main__":
    main()