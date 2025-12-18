import random
import string

def corrupt_data(data, choice):
    if not data:
        return data

    if choice == "1":  # Bit Flip
        char = list(data)
        i = random.randint(0, len(char) - 1)
        bit = ord(char[i]) ^ 1
        char[i] = chr(bit)
        return "".join(char)

    elif choice == "2":  # Character Substitution
        i = random.randint(0, len(data) - 1)
        return data[:i] + random.choice(string.ascii_uppercase) + data[i+1:]

    elif choice == "3":  # Character Deletion
        i = random.randint(0, len(data) - 1)
        return data[:i] + data[i+1:]

    elif choice == "4":  # Random Insertion
        i = random.randint(0, len(data))
        return data[:i] + random.choice(string.ascii_lowercase) + data[i:]

    elif choice == "5":  # Character Swap
        if len(data) < 2:
            return data
        i = random.randint(0, len(data) - 2)
        char = list(data)
        char[i], char[i+1] = char[i+1], char[i]
        return "".join(char)

    elif choice == "6":  # Burst Error
        start = random.randint(0, max(0, len(data) - 3))
        length = random.randint(3, min(8, len(data) - start))
        burst = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        return data[:start] + burst + data[start+length:]

    else:
        return data  # No corruption
