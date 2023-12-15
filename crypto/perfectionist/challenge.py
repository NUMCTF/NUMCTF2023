import base64


# message: 
# MTAwLDExMCw0NDgsODEwNywzMzU1MDM4Nyw4NTg5ODY5MTY2LDEzNzQzODY5MTQyMywyMzA1ODQzMDA4MTM5OTUyMjQ4LDI2NTg0NTU5OTE1Njk4MzE3NDQ2NTQ2OTI2MTU5NTM4NDIyMjQsMTkxNTYxOTQyNjA4MjM2MTA3Mjk0NzkzMzc4MDg0MzAzNjM4MTMwOTk3MzIxNTQ4MTY5MzMw

def func(x):
    y = 0
    for z in range(1, x):
        if x % z == 0:
            y += z
    return y == x

def encr(data_b64):
    i, n = 0, 1
    obf_cipher = base64.b64decode(data_b64).decode().split(",")
    enc_flag = "flag{"
    while i < len(obf_cipher):
        if func(n):
            enc_flag += chr(int(obf_cipher[i]) ^ n)
            i += 1
        n += 1
    enc_flag += "}"
    return enc_flag