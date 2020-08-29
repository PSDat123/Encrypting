def caesar_cipher(content, shift):
    shift = int(shift)
    return ''.join(
        map(chr,
            map(lambda c: 32 if c == " " else ord(c) + shift - (ord(c.lower()) + shift > 122)*26,
                content)))
