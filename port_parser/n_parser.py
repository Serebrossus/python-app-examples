import socket
import argparse

checks = {}


def parse_ports(buf):
    res = []

    if "-" in buf:
        res = [int(i) for i in range(int(buf.split("-")[0]), int(buf.split("-")[1]) + 1)]
    else:
        res = [int(buf)]

    return res


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", type=str, help="target ip-addr")
    parser.add_argument("-p", type=str, help="set port or range with separator '-'")
    return parser


if __name__ == '__main__':
    # init parser. we can use arguments by name
    args = init_parser().parse_args()
    target_ip = args.ip
    # set one port or ports list
    ports = parse_ports(args.p)

    # create socket with params
    for port in ports:
        sock = socket.socket()
        sock.settimeout(3)

        try:
            sock.connect((target_ip, port))
        except:
            checks[target_ip + ":" + str(port)] = "down"
            continue

        checks[target_ip + ":" + str(port)] = "up"
        sock.close()

    # print only 'up' ports
    for i in checks:
        if checks[i] == "up":
            print(i, checks[i])
