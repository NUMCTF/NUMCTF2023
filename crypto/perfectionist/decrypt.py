import base64
from functools import reduce

mersenne = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457]


i = 0
cipher_b64 = b"MTAwLDExMCw0NDgsODEwNywzMzU1MDM4Nyw4NTg5ODY5MTY2LDEzNzQzODY5MTQyMywyMzA1ODQzMDA4MTM5OTUyMjQ4LDI2NTg0NTU5OTE1Njk4MzE3NDQ2NTQ2OTI2MTU5NTM4NDIyMjQsMTkxNTYxOTQyNjA4MjM2MTA3Mjk0NzkzMzc4MDg0MzAzNjM4MTMwOTk3MzIxNTQ4MTY5MzMw"


print("NUMCTF{", end='', flush=True)
cipher = base64.b64decode(cipher_b64).decode().split(",")
while(i < len(cipher)):

        p = 2 ** (mersenne[i] - 1) * (2 ** mersenne[i] - 1)
        print(chr(int(cipher[i]) ^ p),end='', flush=True)
        i += 1

print("}")