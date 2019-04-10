from pwn import *

host = "p1.tjctf.org"

port = 8009

conn =remote(host,port)

r = conn.recv()
print r

e = conn.sendline('one')
print e


