import socket

host = 'ftp.yandex.ru'
port = 21

sock = socket.socket()
try:
    sock.connect( (host, port) )
    print("Sending hello string")
    sock.send("hello\n")
    bufer = sock.recv(1024)
    print(bufer)
    # or print sock.recv(1024)
except Exception as error:
    print(error)
finally:
    sock.close()
