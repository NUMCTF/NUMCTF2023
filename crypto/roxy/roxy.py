flag = bytes('NUM2023{d@mn_y0u_are_s0_r0xy}'.encode('utf-8'))
key = bytes('s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3t'.encode('utf-8'))
result = ''

for i in range(len(flag)):
    result += chr(flag[i] ^ key[i])

print("encoded: ", bytes(result.encode('utf-8')))

# cipher = bytes('\x06G\x05\x1eR\x13\x08G\x0bAl\x04@]<\x1b@+\x1eZ\x04\x1aG\x1d@A<\x06[4\x1dl\x17\x1a\x00+\x0b\\\x11\x0f'.encode('utf-8'))

# cipher1 = result.encode('utf-8')
# cipher1 = bytes('H\x12H,b!;<o\x01\x01j\x1f$\x0cn\x1fJl?[iwB2qD\x7f&N'.encode('utf-8'))
# plain = ''

# for i in range(len(cipher1)):
#     plain += chr(cipher1[i] ^ key[i])

# print(plain)
# print(bytes(plain.encode('utf-8')))
