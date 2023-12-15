def encrypt(plain_text, key):
    cipher_text = ''.join(chr(ord(plain_text[i]) ^ ord(key[i % len(key)])) for i in range(len(plain_text)))
    return cipher_text.encode('utf-8')

def decrypt(cipher_text, key):
    plain_text = ''.join(chr(cipher_text[i] ^ ord(key[i % len(key)])) for i in range(len(cipher_text)))
    return plain_text

plain_text = "NUM2023{d@mn_y0u_are_s0_r0xy}"
encryption_key = "s3cr3t"
encrypted = encrypt(plain_text, encryption_key)
print(f"encrypted: {encrypted}")

decrypt = decrypt(encrypted, encryption_key)
print(f"decrypted: ", {decrypt})