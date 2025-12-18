def generate_checksum(data):
    total = 0
    for c in data:
        total += ord(c)
        total = (total & 0xFFFF) + (total >> 16)
    return format(~total & 0xFFFF, '04X')
