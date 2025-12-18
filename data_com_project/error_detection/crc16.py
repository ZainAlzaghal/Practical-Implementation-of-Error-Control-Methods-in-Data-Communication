def generate_crc16(data):
    poly = 0x1021
    crc = 0xFFFF

    for c in data:
        crc ^= ord(c) << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF

    return format(crc, '04X')
