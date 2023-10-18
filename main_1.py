def hex2string(hex_string):
    result = ''
    for i in range(int(len(hex_string) / 2)):
        selected_hex_string = hex_string[2 * i:2 * i + 2]
        selected_hex_string_integer = int(selected_hex_string, 16)
        result += chr(selected_hex_string_integer)
    return result


def string2hex(input):
    result = ''
    for ch in input:
        ch_int = ord(ch)
        ch_hex = hex(ch_int)
        result += str(ch_hex)[2:]
    return result



def hex_xor(string_one, string_two):
    result = ''
    for i in range(int(len(string_one))):
        ch_one_string = string_one[i]
        # ch_two_string = string_two[i]

        if i % 2 == 0:
            ch_two_string = string_two[0]
        else:
            ch_two_string = string_two[1]
        ch_one_int = int(ch_one_string, 16)
        ch_two_int = int(ch_two_string, 16)
        result += str(hex(ch_one_int ^ ch_two_int))[2:]
    return result


def encrypt_single_byte_xor(text, key):
    result = ''
    for i in range(int(len(text) / int(len(key)))):
        result += hex_xor(text[i*2:i*2+2], key)
    return result


def decrypt_single_byte_xor(text):
    valid_characters = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"
    strings = []
    counts = []
    for i in range(256):
        key = str(hex(i)[2:])
        if i < 16:
            key = '0' + key
        result = encrypt_single_byte_xor(text, key)
        result = hex2string(result)
        strings.append(result)
        count = 0
        for ch in result:
            if ch in valid_characters:
                count += 1
        counts.append(count)
    max_count = -1
    max_idx = -1
    for i in range(int(len(counts))):
        if counts[i] > max_count:
            max_count = counts[i]
            max_idx = i
    return strings[max_idx]

