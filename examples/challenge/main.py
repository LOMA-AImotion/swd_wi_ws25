
one, two = "rdUYjcfruqjUYrfnqAYrfnqPYhtr", "otmsPYitjAYrfnqUYzxPYhtr"

def removeSymbols(msg: str):
    return msg.replace('AY', '@').replace('UY', '-').replace('PY', '.')

def shift(c, s=5):
    lower, upper = ord('a'), ord('z')
    return chr(lower + ((ord(c) - lower - s) % (upper - lower + 1)))

def decrypt(msg, s=5, clean=removeSymbols):
    return ''.join([ shift(c, s) if c.isalnum() else c for c in clean(msg)])
 

print(decrypt(one))
print(decrypt(two))




# Bruteforce the shift
for i in range(1, 26):
    result = decrypt(one, i)
    print(f"{i}:\t {result}")
    if result.endswith('.com'):
        print(f'Shift found: {i}')
        break

