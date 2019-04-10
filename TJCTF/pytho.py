word = input()

p = remote('p1.tjctf.org', 8009)

sa = p.recvuntil('step:')
print sa
sd = p.sendline(word)
print sd 

while True:
    line = p.recvline()
    print(line)
    line = line[14:-2]
    p.recvuntil('step:')
    p.sendline(line)

    
