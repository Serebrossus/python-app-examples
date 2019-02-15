import socket

host = 'ftp.yandex.ru'
port = 21

sock = socket.socket()
try:
    sock.connect((host, port))
    print("Sending hello string")
    sock.send("hello \n")
    buffer = sock.recv(1024)
    print(buffer)
    # or print sock.recv(1024)
except Exception as error:
    print(error)
finally:
    sock.close()
