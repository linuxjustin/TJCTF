from pwn import *

host = "p1.tjctf.org"

port = 8009

conn = remote(host,port)

conn.recvuntil("Encountered ")

data = conn.recvuntil('\n').replace("'","")

print data
conn.recv()
conn.recv()
#s = conn.recvuntil("The First step: ")
print s
conn.sendline(data)
print a
print conn.recv()
print conn.recv()


