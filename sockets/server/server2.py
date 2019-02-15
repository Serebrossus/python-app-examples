import socket
import socketserver
import sys
from hashlib import md5
import threading
import time



password_hash = '5f4dcc3b5aa765d61d8327deb882cf99'


# Async Mixin from SocketServer documentation
class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.request.sendall("Auth panel\nEnter username: ".encode('utf-8'))
        username = self.request.recv(1024).strip()

        print("username: " + username.decode('utf-8'))

        if username.decode('utf-8') != 'admin':
            self.request.sendall("[-] Username is invalid\nExit".encode('utf-8'))
            return -1

        self.request.sendall("Enter password: ".encode('utf-8'))

        password = self.request.recv(1024).strip()

        print("password: " + password.decode('utf-8'))

        hashed_password = md5(password).hexdigest()

        if hashed_password != password_hash:
            self.request.sendall("[-] Password is invalid\nExit".encode('utf-8'))
            return -2

        self.request.sendall("Welcome Admin\n".encode('utf-8'))

        data = self.request.recv(1024)

        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response.encode('utf-8'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        print("Usage python " + sys.argv[0] + " <port>")
        sys.exit(-1)

    HOST = '0.0.0.0'
    PORT = port

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server = ThreadedTCPServer((HOST, PORT), RequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = False
    server_thread.start()

    print("Server loop running in thread:", server_thread.name)

    while True:
        try:
            time.sleep(1)
        except Exception as e:
            print(e)
            break

    print("start server shutdown process")
    server.shutdown()
    server.server_close()
