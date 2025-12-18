def generate_parity(data):
    bits = ''.join(format(ord(c), '08b') for c in data)
    ones = bits.count('1')
    return "0" if ones % 2 == 0 else "1"
