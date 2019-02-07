capital_letters = ord("A")
capital_z = ord("Z")

def encrypt(msg, key):
    msg = list(msg.upper())
    for a in range(0, len(msg), 1):
        if "A" <= msg[a] <= "Z":
            msg[a] = chr(capital_letters + (ord(msg[a]) - capital_letters + key)%26)
    return "".join(msg)

def decrypt(msg, key):
    msg = list(msg.upper())
    for a in range(0, len(msg), 1):
        if "A" <= msg[a] <= "Z":
            msg[a] = chr(capital_z - (capital_z - ord(msg[a]) - 26 + key)%26)
    return "".join(msg)


msg = "Bruce Wayne är Batman!"
print(encrypt(msg, 17))
print(decrypt(encrypt(msg, 17), 17))