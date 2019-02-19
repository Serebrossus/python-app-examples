import socket
import argparse
import threading
from queue import Queue

checks = {}
TIMEOUT = 5
hostPort_queue = None


def scan_port(host, port):
    sock = socket.socket()
    sock.settimeout(TIMEOUT)
    try:
        sock.connect((host, port))
        checks[host + ":" + str(port)] = "up"
    except:
        checks[host + ":" + str(port)] = "down"

    sock.close()


def runner():
    while 1:
        host, port = hostPort_queue.get()
        scan_port(host, port)
        hostPort_queue.task_done()


def parse_ports(buf):
    # res = []
    if '-' in buf:
        split_buff = buf.split('-')
        # asc sort list
        custom_list = list(map(int, split_buff))
        custom_list.sort()
        # aka res.append(int(i))
        res = [int(i) for i in range(int(custom_list[0]), int(custom_list[1]) + 1)]
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
    # for debug
    # for port in ports:
    #     print('parsed port: ', port)

    hostPort_queue = Queue()

    for _ in range(50):
        thread = threading.Thread(target=runner)
        thread.daemon = True
        thread.start()

    for port in ports:
        hostPort_queue.put((target_ip, port))

    hostPort_queue.join()

    # print only 'up' ports
    for i in checks:
        if checks[i] == "up":
            print(i, checks[i])
