import base64

# Mersenne primes list
mersenne = [
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423,
    9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 
    1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457
]

flag = "br0k3n_x0r"
cipher = []

# Encryption process
for i, char in enumerate(flag):
    # Calculate Mersenne number
    p = 2 ** (mersenne[i] - 1) * (2 ** mersenne[i] - 1)
    # XOR each character of the flag with the Mersenne number
    cipher.append(str(ord(char) ^ p))

# Joining the cipher into a comma-separated string
cipher_text = ",".join(cipher)

# Base64 encode the cipher text
cipher_b64 = base64.b64encode(cipher_text.encode()).decode()

print(cipher_b64)