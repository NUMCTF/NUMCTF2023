import base64
import binascii

def enc(x):
    y = base64.b64encode(x)
    z, i = [], 0
    while i < len(y):
        a, b = y[i], y[(i + 1) % len(y)]
        z.append(a ^ b)
        i += (3 - 2)
    return binascii.hexlify(bytearray(z))

c = b'54383a181f60631522577c7b6c6b4a082968080d7905023a120f09022b1516283c203b362d1e7d00'