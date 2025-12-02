ELVISH_MAP = {
    'a': 'ae',
    'b': 'bel',
    'c': 'cal',
    'd': 'dor',
    'e': 'el',
    'f': 'fin',
    'g': 'gal',
    'h': 'hel',
    'i': 'il',
    'j': 'jar',
    'k': 'kel',
    'l': 'lin',
    'm': 'mir',
    'n': 'nor',
    'o': 'or',
    'p': 'pal',
    'q': 'quar',
    'r': 'rin',
    's': 'sil',
    't': 'tin',
    'u': 'uil',
    'v': 'vel',
    'w': 'wen',
    'x': 'xael',
    'y': 'yar',
    'z': 'zir',
}

# Inverse map for decoding
ELVISH_REVERSE_MAP = {v: k for k, v in ELVISH_MAP.items()}

def to_elvish(text: str) -> str:
    text = text.lower()   # we limit to lowercase as required
    secret_words = []

    for word in text.split(" "):          # keep word boundaries
        encoded_letters = []
        for ch in word:
            if ch in ELVISH_MAP:          # only encode letters a–z
                encoded_letters.append(ELVISH_MAP[ch])
            else:
                encoded_letters.append(ch)  # keep punctuation/digits as-is
        secret_words.append("-".join(encoded_letters))
    
    return " ".join(secret_words)

def from_elvish(secret_text: str) -> str:
    normal_words = []

    for word in secret_text.split(" "):   # split encoded words
        parts = word.split("-") if word else []
        decoded_letters = []
        for part in parts:
            if part in ELVISH_REVERSE_MAP:
                decoded_letters.append(ELVISH_REVERSE_MAP[part])
            else:
                decoded_letters.append(part)  # pass through punctuation/digits
        normal_words.append("".join(decoded_letters))
    
    return " ".join(normal_words)
def from_elvish(secret_text: str) -> str:
    normal_words = []

    for word in secret_text.split(" "):   # split encoded words
        parts = word.split("-") if word else []
        decoded_letters = []
        for part in parts:
            if part in ELVISH_REVERSE_MAP:
                decoded_letters.append(ELVISH_REVERSE_MAP[part])
            else:
                decoded_letters.append(part)  # pass through punctuation/digits
        normal_words.append("".join(decoded_letters))
    
    return " ".join(normal_words)

sentence = "meet me in mordor."
secret = to_elvish(sentence)
back = from_elvish(secret)

print("Original:", sentence)
print("Elvish:  ", secret)
print("Decoded: ", back)
