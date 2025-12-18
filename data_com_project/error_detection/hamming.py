def to_binary(data):
    return ''.join(format(ord(c), '08b') for c in data)


def from_binary(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


def hamming_encode_4bits(bits):
    d1, d2, d3, d4 = map(int, bits)

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    return f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"


def hamming_decode_7bits(bits):
    b = list(map(int, bits))

    p1 = b[0] ^ b[2] ^ b[4] ^ b[6]
    p2 = b[1] ^ b[2] ^ b[5] ^ b[6]
    p3 = b[3] ^ b[4] ^ b[5] ^ b[6]

    error_pos = p1 * 1 + p2 * 2 + p3 * 4

    corrected = False
    if error_pos != 0:
        b[error_pos - 1] ^= 1
        corrected = True

    data_bits = f"{b[2]}{b[4]}{b[5]}{b[6]}"
    return data_bits, corrected, error_pos


def generate_hamming(data):
    binary = to_binary(data)
    encoded = ""

    for i in range(0, len(binary), 4):
        encoded += hamming_encode_4bits(binary[i:i+4])

    return encoded


def check_and_correct_hamming(encoded):
    decoded = ""
    corrected_any = False
    error_positions = []

    for i in range(0, len(encoded), 7):
        bits = encoded[i:i+7]
        data_bits, corrected, pos = hamming_decode_7bits(bits)
        decoded += data_bits
        if corrected:
            corrected_any = True
            error_positions.append(pos)

    return from_binary(decoded), corrected_any, error_positions
