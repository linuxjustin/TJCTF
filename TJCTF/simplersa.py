def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m





p = 564819669946735512444543556507
 
q = 671998030559713968361666935769

n = 379557705825593928168388035830440307401877224401739990998883
e = 65537
c = 29031324384546867512310480993891916222287719490566042302485

fi = (p-1)*(q-1)
d = modinv(e, fi)
print ("%x" % pow(c, d, n)).decode("hex")