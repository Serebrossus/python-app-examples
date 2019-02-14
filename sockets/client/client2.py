from pwn import *

host = '127.0.0.1'
port = 80

r =remote(host, port)
# examples
data = r.recv()
data = r.recv(1024)
data = r.recv('Test: ')

r.send("123\n")
r.sendline("123")

# run interactive mode
r.interactive()