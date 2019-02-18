import socket
import argparse
import threading
from queue import Queue

checks = {}
timeout = 4
hostPort_queue = None


def scanPort(host, port):
    sock = socket.socket()
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        checks[host + ":" + str(port)] = "up"
    except:
        checks[host + ":" + str(port)] = "down"

    sock.close()


def runner():
    while 1:
        host, port = hostPort_queue.get()
        scanPort(host, port)
        hostPort_queue.task_done()


def parsePorts(buf):
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
    ports = parsePorts(args.p)

    hostPort_queue = Queue()

    for _ in range(50):
        thread = threading.Thread(target=runner())
        thread.deamon = True
        thread.start()

    for port in ports:
        hostPort_queue.put((target_ip, port))

    hostPort_queue.join()


    # print only 'up' ports
    for i in checks:
        if checks[i] == "up":
            print(i, checks[i])
