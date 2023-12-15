import binascii
import base64

def decrypt(cipher_hex):
    # hex to bytes
    cipher_bytes = binascii.unhexlify(cipher_hex)

    # reverse cyclic XOR
    xor_result = bytearray([cipher_bytes[0]])
    for i in range(1, len(cipher_bytes)):
        xor_result.append(cipher_bytes[i] ^ xor_result[i - 1])

    # base 64 decode
    try:
        decoded_flag = base64.b64decode(xor_result)
        return decoded_flag
    except Exception as e:
        return f"error: {e}"

cipher = b"54383a181f60631522577c7b6c6b4a082968080d7905023a120f09022b1516283c203b362d1e7d00"
print(decrypt(cipher))

