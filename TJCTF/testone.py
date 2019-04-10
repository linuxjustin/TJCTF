#!/usr/bin/python 

from pwn import * 
import string

# p1.tjctf.org 8009


s = remote('p1.tjctf.org',8009) 
print s.recv()
s.sendline ('one')

response = str(s.recv())
print response



while ( 1 ):

        

        

        r1 = response.replace('Encountered','')
        r1 = r1.replace("'",'')
        #print r1
        r1 = r1.replace("\nThe next step:",'').replace(" ","")
        #print r1
        #r1 = r1.replace("'",'')

        
        #responseword = response.replace('Encountered','')
        #responseword = responseword.replace(' ','')
        #responseword = responseword.replace(''','')
        #responseword = responseword.replace('\nThenextstep:','')
        #responseword = responseword.replace(''','')
        #print ('response word is',r1)
        s.sendline (r1)
        response = s.recv()
        s.clean(0)  
        print ('still running...')

        print response 

        if "ctf" in response: 
            print response
            print ('done !!!!')
            break

s.close()


