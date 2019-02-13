import socket
import time
import sys

# in directory enter python server1.py in terminal
if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        print("Usage python " + sys.argv[0] + ' <port>')
        sys.exit(-1)

host = '0.0.0.0'
sock_server = socket.socket()
try:
    sock_server.bind((host, port))
    sock_server.listen(3)
    for i in range(0, 11):
        conn, addr = sock_server.accept()

        if conn:
            conn.sendall(str(time.time()) + '\n')
            conn.close()

except Exception as e:
    print(e)
finally:
    print("close sock server")
    sock_server.close()