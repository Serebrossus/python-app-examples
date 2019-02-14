import socketserver
import sys
# from hashlib import md5
import threading
import time


# Async Mixin from SocketServer documentation
class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
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
